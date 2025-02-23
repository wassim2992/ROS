import rclpy
from rclpy.node import Node
import random  
from std_msgs.msg import Int32  

class CapteurPresence(Node):
    def __init__(self):
        super().__init__('capteur_presence')
        self.publisher_ = self.create_publisher(Int32, 'presence', 10)
        self.timer = self.create_timer(2.0, self.publier_presence)  

    def publier_presence(self):
        presence = random.choice([0, 1])  
        msg = Int32()
        msg.data = presence
        self.publisher_.publish(msg)
        etat = "y a un reuf" if presence == 1 else "y a personne frr"
        self.get_logger().info(f'{etat} (Valeur = {presence})')

def main(args=None):
    rclpy.init(args=args)
    node = CapteurPresence()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

