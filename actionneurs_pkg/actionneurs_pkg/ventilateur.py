import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Ventilateur(Node):
    def __init__(self):
        super().__init__('ventilateur')
        self.subscription = self.create_subscription(
            Int32,
            'commande_ventilateur',
            self.commande_callback,
            10)
        self.publisher_ = self.create_publisher(Int32, 'commande_ventilateur', 10)
        self.etat = "OFF"

    def commande_callback(self, msg):
        niveaux = {0: "OFF", 1: "niv1", 2: "niv2", 3: "niv3"}
        if msg.data in niveaux:
            self.etat = niveaux[msg.data]
            self.get_logger().info(f'Ventilateur : {self.etat}')

            
            msg_pub = Int32()
            msg_pub.data = msg.data 
            self.publisher_.publish(msg_pub)
        else:
            self.get_logger().warn("C'est 0, 1, 2 ou 3")

def main(args=None):
    rclpy.init(args=args)
    node = Ventilateur()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

