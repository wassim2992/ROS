import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger 

class TemperatureServer(Node):
    def __init__(self):
        super().__init__('temperature_server')
        self.srv = self.create_service(Trigger, 'get_temperature', self.get_temperature_callback)

    def get_temperature_callback(self, request, response):
 
        temperature = 20.5  
        self.get_logger().info(f"recu mec la temp est de: {temperature} °C")
        response.success = True
        response.message = f"{temperature} °C"
        return response

def main():
    rclpy.init()
    node = TemperatureServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

