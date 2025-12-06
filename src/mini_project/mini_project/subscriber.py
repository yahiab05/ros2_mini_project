import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatteryTempSubscriber(Node):
    def __init__(self):
        super().__init__("battery_temp_subscriber")
        self.subscription = self.create_subscription(Float32, "battery_temp", self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        
        self.emergency_cooler_on = False
        self.emojies = {"fire": "\U0001F525",
                        "check": "\u2714",
                        "warning": "\u26A0"}
        
    def listener_callback(self, msg):
        temp = msg.data
        self.emergency_cooler_on = temp > 75
        
        if self.emergency_cooler_on:
            self.get_logger().info("The emergency cooler is on")
            temp -= 10
        
        if 20 <= temp < 55:
            self.get_logger().info(self.template_log("check", temp, "OK"))
        elif 55 <= temp < 75:
            self.get_logger().info(self.template_log("warning", temp, "high but not critical"))
        elif 75 <= temp <= 90:
            self.get_logger().info(self.template_log("fire", temp, "critical"))
        else:
            self.get_logger().info("")
            
    def template_log(self, emoji_type: str, temp, state:str):
        return f"{self.emojies[emoji_type]}: The temperature is {state} at {temp}°C"
        

def main():
    rclpy.init()
    subscriber = BatteryTempSubscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()