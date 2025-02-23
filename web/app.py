import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from flask import Flask, render_template, jsonify, request
import threading
import random
import time

app = Flask(__name__, template_folder='templates')


capteurs = {
    "temperature": 20.0,  
    "humidite": 50.0,  
    "presence": 0,  
    "ventilateur": 0,  
    "led": 0  
}

class CapteurListener(Node):
    def __init__(self):
        super().__init__('capteur_listener')
        self.create_subscription(Int32, 'temperature', self.update_temperature, 10)
        self.create_subscription(Int32, 'humidite', self.update_humidite, 10)
        self.create_subscription(Int32, 'presence', self.update_presence, 10)

    def update_temperature(self, msg):
        capteurs["temperature"] = msg.data

    def update_humidite(self, msg):
        capteurs["humidite"] = msg.data

    def update_presence(self, msg):
        capteurs["presence"] = msg.data
        capteurs["led"] = 1 if msg.data == 1 else 0

class WebControlNode(Node):
    def __init__(self):
        super().__init__('web_control')
        self.pub_ventilateur = self.create_publisher(Int32, 'commande_ventilateur', 10)
        self.pub_led = self.create_publisher(Int32, 'commande_led', 10)

    def envoyer_commande_ventilateur(self, valeur):
        capteurs["ventilateur"] = valeur  
        msg = Int32()
        msg.data = valeur
        self.pub_ventilateur.publish(msg)

    def envoyer_commande_led(self, valeur):
        capteurs["led"] = valeur  
        msg = Int32()
        msg.data = valeur
        self.pub_led.publish(msg)

@app.route('/')
def home():
    return render_template('debut.html')

@app.route('/capteurs')
def get_capteurs():
    return jsonify(capteurs)

@app.route('/commande_ventilateur', methods=['POST'])
def commande_ventilateur():
    data = request.json.get('data')
    node_web.envoyer_commande_ventilateur(data)
    return jsonify({"message": "Commande ventilateur envoyée", "valeur": data})

@app.route('/commande_led', methods=['POST'])
def commande_led():
    data = request.json.get('data')
    node_web.envoyer_commande_led(data)
    return jsonify({"message": "Commande LED envoyée", "valeur": data})

def simulateur_capteurs():
    """ Simule les variations progressives des capteurs toutes les secondes. """
    while True:
        capteurs["temperature"] += random.uniform(-0.5, 0.5)
        capteurs["temperature"] = max(15, min(35, capteurs["temperature"]))  

        capteurs["humidite"] += random.uniform(-1, 1)
        capteurs["humidite"] = max(30, min(70, capteurs["humidite"]))  

        if random.randint(1, 10) > 8:  
            capteurs["presence"] = 1
            capteurs["led"] = 1  
        else:
            capteurs["presence"] = 0
            capteurs["led"] = 0 
        if capteurs["temperature"] > 30:
            capteurs["ventilateur"] = 3
        elif capteurs["temperature"] > 27:
            capteurs["ventilateur"] = 2
        elif capteurs["temperature"] > 24:
            capteurs["ventilateur"] = 1
        else:
            capteurs["ventilateur"] = 0
        time.sleep(1) 



if __name__ == '__main__':
    rclpy.init()


    node_web = WebControlNode()
    ros2_thread = threading.Thread(target=rclpy.spin, args=(node_web,), daemon=True)
    ros2_thread.start()
    capteur_thread = threading.Thread(target=simulateur_capteurs, daemon=True)
    capteur_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=True)

