import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  

class LED(Node):
    def __init__(self):
        super().__init__('led')
        self.subscription = self.create_subscription(
            Int32,
            'commande_led',
            self.commande_callback,
            10)
        self.publisher_ = self.create_publisher(Int32, 'commande_led', 10)  
        self.etat = "OFF" 

    def commande_callback(self, msg):
        if msg.data == 0:
            self.etat = "OFF"
        elif msg.data == 1:
            self.etat = "ON"
        else:
            self.get_logger().warn('c est 0 ou 1 le reuf')
            return

        
        msg_pub = Int32()
        msg_pub.data = msg.data  
        self.publisher_.publish(msg_pub)

        self.get_logger().info(f'LED : {self.etat}')

def main(args=None):
    rclpy.init(args=args)
    node = LED()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


