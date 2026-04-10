##!/usr/bin/env python3
 
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random
 
def main(args=None):
    
    rclpy.init(args=args)
    node = Node('simple_spawner')
    client = node.create_client(Spawn, '/spawn')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('Attente du service /spawn...')
    x = random.uniform(1.0, 10.0)      
    y = random.uniform(1.0, 10.0)
    theta = random.uniform(0.0, 6.283) 
    request = Spawn.Request()
    request.x = x
    request.y = y
    request.theta = theta
    request.name = "turtle_target"
    node.get_logger().info(f"Spawn de turtle_target a x={x:.2f}, y={y:.2f}")
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        node.get_logger().info(f" Tortue '{future.result().name}' cree avec succes!")
    else:
        node.get_logger().error(f" Erreur : {future.exception()}")
    node.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()