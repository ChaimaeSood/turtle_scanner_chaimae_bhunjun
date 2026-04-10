#!/usr/bin/env python3
 
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random
 
class ColoredSpawn(Node):
    def __init__(self):
        super().__init__('colored_spawn')
        self.spawn_client = self.create_client(Spawn, '/spawn')
    def spawn_turtle_target(self):
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service /spawn non disponible...')
        x = random.uniform(1.0, 10.0)
        y = random.uniform(1.0, 10.0)
        theta = random.uniform(0.0, 6.283)
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = "turtle_target"
        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.display_coordinates(x, y, theta)
            return True
        else:
            self.get_logger().error(" Spawn echoue!")
            return False
    def display_coordinates(self, x, y, theta):
        """Affiche les coordonnees de manière formatee."""
        separator = * 50
        self.get_logger().info(separator)
        self.get_logger().info(" SPAWN REUSSI - TURTLE_TARGET CREEE ")
        self.get_logger().info(separator)
        self.get_logger().info("")
        self.get_logger().info("COORDONNEES CARTESIENNES :")
        self.get_logger().info(f"   • X = {x:.3f}")
        self.get_logger().info(f"   • Y = {y:.3f}")
        self.get_logger().info("")
        self.get_logger().info("ORIENTATION :")
        self.get_logger().info(f"   • Radians : {theta:.3f}")
        self.get_logger().info(f"   • Degres  : {theta * 180 / 3.14159:.1f}°")
        self.get_logger().info("")
        self.get_logger().info(separator)
 
def main(args=None):
    rclpy.init(args=args)
    node = ColoredSpawn()
    node.spawn_turtle_target()
    rclpy.spin_once(node, timeout_sec=1.0)
    node.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
 