import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Adapter selon le type de message utilisé

class MonSubscriber(Node):
    def __init__(self):
        super().__init__('mon_subscriber')

        # Création du Subscriber qui écoute le topic "test_topic"
        self.subscription = self.create_subscription(
            String,  # Type de message
            'test_topic',  # Nom du topic
            self.listener_callback,  # Fonction callback exécutée à la réception d'un message
            10)
        self.subscription  # Évite un warning inutile

    def listener_callback(self, msg):
        """ Fonction exécutée lorsqu'un message est reçu """
        self.get_logger().info(f"Message reçu : {msg.data}")

        # Exemple d'utilisation du message reçu
        if msg.data.lower() == "on":
            self.get_logger().info("Commande reçue : Activer un actionneur")
        elif msg.data.lower() == "off":
            self.get_logger().info("Commande reçue : Désactiver un actionneur")
        else:
            self.get_logger().warn("Commande inconnue reçue")

def main(args=None):
    rclpy.init(args=args)
    node = MonSubscriber()
    rclpy.spin(node)  # Permet au Subscriber d'écouter en continu
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

