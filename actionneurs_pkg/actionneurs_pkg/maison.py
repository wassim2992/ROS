import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class GestionMaison(Node):
    def __init__(self):
        super().__init__('maison')

        
        self.mode_automatique = True

     
        self.subscription_temp = self.create_subscription(Int32, 'temperature', self.callback_temperature, 10)
        self.subscription_humidite = self.create_subscription(Int32, 'humidite', self.callback_humidite, 10)
        self.subscription_presence = self.create_subscription(Int32, 'presence', self.callback_presence, 10)
        self.subscription_mode = self.create_subscription(Int32, 'mode', self.callback_mode, 10)

       
        self.pub_ventilateur = self.create_publisher(Int32, 'commande_ventilateur', 10)
        self.pub_led = self.create_publisher(Int32, 'commande_led', 10)


        self.ventilateur_niveau = 0
        self.led_etat = 0

    def callback_temperature(self, msg):
        if self.mode_automatique:
            if msg.data > 30:
                temp_niveau = 3  
            elif msg.data > 27:
                temp_niveau = 2  
            elif msg.data > 24:
                temp_niveau = 1  
            else:
                temp_niveau = 0  

            self.mettre_a_jour_ventilateur(temp_niveau)

    def callback_humidite(self, msg):
        if self.mode_automatique:
            if msg.data > 70:
                humid_niveau = 3  
            elif msg.data > 60:
                humid_niveau = 2  
            elif msg.data > 50:
                humid_niveau = 1  
            else:
                humid_niveau = 0  

            self.mettre_a_jour_ventilateur(humid_niveau)

    def callback_presence(self, msg):
        if self.mode_automatique:
            if msg.data == 1:
                self.led_etat = 1  
            else:
                self.led_etat = 0  

            self.pub_led.publish(Int32(data=self.led_etat))
            self.get_logger().info(f"y a un mec -> LED {'ON' if self.led_etat else 'OFF'}")

    def callback_mode(self, msg):
        self.mode_automatique = (msg.data == 1)
        mode = "Automatique" if self.mode_automatique else "Manuel"
        self.get_logger().info(f"Mode changé : {mode}")

    def mettre_a_jour_ventilateur(self, nouveau_niveau):
    
        if nouveau_niveau > self.ventilateur_niveau:
            self.ventilateur_niveau = nouveau_niveau
        else:
            self.ventilateur_niveau = max(self.ventilateur_niveau, nouveau_niveau)

        self.pub_ventilateur.publish(Int32(data=self.ventilateur_niveau))
        self.get_logger().info(f"Ventilateur -> Niveau {self.ventilateur_niveau}")

def main(args=None):
    rclpy.init(args=args)
    node = GestionMaison()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

