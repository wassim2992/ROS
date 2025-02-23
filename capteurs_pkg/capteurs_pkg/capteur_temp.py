import rclpy
from rclpy.node import Node
import random  
from std_msgs.msg import Float32  

class CapteurTemperature(Node):
    def __init__(self):
        super().__init__('capteur_temperature')
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        self.timer = self.create_timer(2.0, self.publier_temperature)   secondes

    def publier_temperature(self):
        temperature = random.uniform(20.0, 30.0)  
        msg = Float32()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info(f'il fait : {temperature:.2f}°C')

def main(args=None):
    rclpy.init(args=args)
    node = CapteurTemperature()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

