import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Adapter selon le type de message utilisé

class MonPublisher(Node):
    def __init__(self):
        super().__init__('mon_publisher')

        # Création du Publisher qui envoie des messages sur "test_topic"
        self.publisher = self.create_publisher(String, 'test_topic', 10)

        # Timer pour envoyer un message toutes les 2 secondes
        self.timer = self.create_timer(2.0, self.publish_message)

    def publish_message(self):
        """ Fonction qui envoie un message à intervalle régulier """
        msg = String()
        msg.data = "ON"  # Peut être changé pour un autre message
        self.publisher.publish(msg)
        self.get_logger().info(f"Message envoyé : {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = MonPublisher()
    rclpy.spin(node)  # Le Publisher envoie des messages en continu
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

