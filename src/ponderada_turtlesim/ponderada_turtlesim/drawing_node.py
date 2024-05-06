# O seguinte código foi feito com o auxílio da IA generativa ChatGPT
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
from math import radians
import time

class CircleTurtle(Node):

    def __init__(self):
        super().__init__('circle_turtle')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Nasce uma nova tartaruga
        self.spawn_turtle()

        # Configura a cor e a espessura da caneta
        self.set_pen(0, 255, 255, 5, 0)

        # Move a tartaruga em um círculo
        self.move_circle()

        # Mata a tartaruga
        self.kill_turtle()

    def spawn_turtle(self):
        spawn_client = self.create_client(Spawn, 'spawn')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço "spawn" não disponível, esperando...')

        request = Spawn.Request()
        request.x = float(2)
        request.y = float(2)
        request.theta = float(0)
        request.name = 'turtle1'

        spawn_future = spawn_client.call_async(request)
        while rclpy.ok():
            rclpy.spin_once(self)
            if spawn_future.done():
                try:
                    response = spawn_future.result()
                except Exception as e:
                    self.get_logger().error(f'Falha ao nascer a nova tartaruga: {str(e)}')
                break

    def set_pen(self, r, g, b, width, off):
        set_pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        while not set_pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço "/turtle1/set_pen" não disponível, esperando...')

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        response_future = set_pen_client.call_async(request)
        while rclpy.ok():
            rclpy.spin_once(self)
            if response_future.done():
                try:
                    response = response_future.result()
                except Exception as e:
                    self.get_logger().error(f'Falha ao configurar a caneta: {str(e)}')
                break

    def move_circle(self):
        
        vel_msg = Twist()
        vel_msg.linear.x = float(1)
        vel_msg.angular.z = float(1)

        start_time = time.time()
        while time.time() - start_time < 6:  # Desenha o círculo por 6 segundos
            self.publisher_.publish(vel_msg)
            time.sleep(0.1)

        # Quando o tempo de execução acabar, paramos a tartaruga
        vel_msg.linear.x = float(0)
        vel_msg.angular.z = float(0)
        self.publisher_.publish(vel_msg)

    def kill_turtle(self):
        kill_client = self.create_client(Kill, 'kill')
        while not kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço "kill" não disponível, esperando...')

        request = Kill.Request()
        request.name = 'turtle1'

        kill_future = kill_client.call_async(request)
        while rclpy.ok():
            rclpy.spin_once(self)
            if kill_future.done():
                try:
                    response = kill_future.result()
                except Exception as e:
                    self.get_logger().error(f'Falha ao matar a tartaruga: {str(e)}')
                break

def main(args=None):
    rclpy.init(args=args)

    circle_turtle = CircleTurtle()

    rclpy.spin(circle_turtle)

    circle_turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
