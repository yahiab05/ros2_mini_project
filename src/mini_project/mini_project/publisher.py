import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from random import random

class BatteryTempPublisher(Node):
    def __init__(self):
        super().__init__("battery_temp_publisher")
        self.publisher = self.create_publisher(Float32, "battery_temp", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.temperature = 20
        
    def timer_callback(self):
        msg = Float32()
        self.increase_temp()
        msg.data = float(self.temperature)
        self.publisher.publish(msg)
        
    def increase_temp(self):
        increase_factor = 0
        increase_rate = 0
        cooling_factor = 0
        
        if self.temperature < 55:
            increase_factor = 1
            increase_rate = 0.9
        elif 55 <= self.temperature < 65:
            increase_factor = 0.8
            increase_rate = 0.5
            cooling_factor = 0.1
        elif 65 <= self.temperature <= 75:   
            increase_factor = 0.1
            increase_rate = 0.1
            cooling_factor = 0.2
        elif 75 < self.temperature <= 90:
            increase_factor = 0.1
            increase_rate = 0.01
            cooling_factor = 0.2
        else:
            cooling_factor = 1
            
        if random() < increase_rate:
            self.temperature += increase_factor
            
        self.temperature -= cooling_factor
        
def main():
    try:
        rclpy.init()
        publisher = BatteryTempPublisher()
        rclpy.spin(publisher)
    except KeyboardInterrupt:
        publisher.destroy_node()
    
if __name__ == "__main__":
    main()
