import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class TemperatureClient(Node):
    def __init__(self):
        super().__init__('temperature_client')
        self.cli = self.create_client(Trigger, 'get_temperature')

    def request_temperature(self):
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('en att le reuf')
        req = Trigger.Request()
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main():
    rclpy.init()
    node = TemperatureClient()
    response = node.request_temperature()
    if response:
        node.get_logger().info(f"on a: {response.message}")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

