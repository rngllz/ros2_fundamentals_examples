#! /usr/bin/env python3

"""
  Drescription:
      A minimal ROS 2 publisher node in Python that publishes "Hello World!" messages to a topic.

  -------
  Publishing Topics:
      The channel containing the "Hello World!" messages
      /py_example_topic - std_msgs/String

  -------
  Subscription Topics:
      None

  -------
  Author: Luca Mateo Rangel
  Date: 10 Janeiro, 2026
"""

import rclpy  # import the' ROS 2 client library for python
from rclpy.node import Node  # Import the Node class, used for creating nodes
from std_msgs.msg import String  # Import String message type from ROS 2


class MinimalPublisher(Node):
    """
      Create a minimal publisher node.
    """

    def __init__(self):
        """
          Create a custom node class for publishing messages.
        """
        # Initialize the node with a name
        super().__init__('minimal_publisher')  # Initialize the node with the name 'minimal_publisher'

        # Create a publisher on the topic with a queue size of 10 messages
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        # Create a timer with a period of 0.5 seconds to trigger publishing of message
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Initialize a counter variable for a message content
        self.i = 0

    def timer_callback(self):
        """
          Callback function for the timer.Call back function executed periodically by the timer
        """
        # Create a new String message object
        msg = String()

        # Set the message data with a counter
        msg.data = 'Olá Mundo! %d' % self.i

        # Publish the message you created above to a topic
        self.publisher_1.publish(msg)

        # Log a message inidicating the message has been published
        self.get_logger().info('Publishing: "%s' % msg.data)
        self.i += 1


def main(args=None):
    """
      Main function to start the ROS 2 node

      Args:
          args (List, optional): Command-line arguments. Defaults to None.
    """
    rclpy.init(args=args)

    # Create an instance of the Minimal Publisher node
    minimal_py_publisher = MinimalPublisher()

    rclpy.spin(minimal_py_publisher)

    # Destroy the node explicitly
    minimal_py_publisher.destroy_node()

    # Shutdown RO 2 communication
    rclpy.shutdown()


if __name__ == '__main__':
    # Execute the main function  if the script is run directly
    main()
