#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random

class SpawnTarget(Node):

def __init__(self):
    super().__init__('spawn_target')

    # Create client for /spawn service
    self.client = self.create_client(Spawn, '/spawn')

    # Wait for service to be available
    while not self.client.wait_for_service(timeout_sec=1.0):
        self.get_logger().info('Waiting for /spawn service...')

    # Generate random coordinates
    x = random.uniform(1.0, 10.0)
    y = random.uniform(1.0, 10.0)
    theta = random.uniform(0.0, 3.14)

    # Create request
    request = Spawn.Request()
    request.x = x
    request.y = y
    request.theta = theta
    request.name = 'turtle_target'

    # Call service
    future = self.client.call_async(request)
    future.add_done_callback(self.callback_response)

def callback_response(self, future):
    try:
        response = future.result()
        self.get_logger().info(
            f"Turtle spawned at random position!"
        )
    except Exception as e:
        self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
rclpy.init(args=args)
node = SpawnTarget()
rclpy.spin(node)
rclpy.shutdown()

if name == 'main':
main(
