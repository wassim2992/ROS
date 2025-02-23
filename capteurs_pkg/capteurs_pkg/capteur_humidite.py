import rclpy
from rclpy.node import Node
import random  
from std_msgs.msg import Float32  

class CapteurHumidite(Node):
    def __init__(self):
        super().__init__('capteur_humidite')
        self.publisher_ = self.create_publisher(Float32, 'humidite', 10)
        self.timer = self.create_timer(2.0, self.publier_humidite)  

    def publier_humidite(self):
        humidite = random.uniform(30.0, 80.0)  
        msg = Float32()
        msg.data = humidite
        self.publisher_.publish(msg)
        self.get_logger().info(f'on a une humidite de: {humidite:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node = CapteurHumidite()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

