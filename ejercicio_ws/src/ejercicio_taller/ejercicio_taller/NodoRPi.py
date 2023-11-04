import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32, Bool, String

class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')

        # Create Publishers
        self.publisher_proxomidad = self.create_publisher(Float32, "/distancia_sensor",10)
        self.publisher_boton = self.create_publisher(Bool, "/estado_boton",10)

        # Create Subscribers
        self.subscriber_LED = self.create_subscription(Bool,"/estado_LED",self.callback_sub_LED,10)
        self.subscriber_servo = self.create_subscription(Int32,"/pwm_servo", self.callback_sub_servo,10)

        self.subscriber_test = self.create_subscription(String,"/topic_test",self.callback_sub_test,10)

        # Initialize attributes
        self.estado_LED = True
        self.distancia_sensor = 0.0
        self.estado_boton = False
        self.pwm_servo = 0

        # pins setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT) #LED
        GPIO.setup(13,GPIO.OUT) #PWM al servo 
        self.servo = GPIO.PWM(13,100)
        self.servo.start(100)
        self.servo.ChangeDutyCycle(10)

        # Create timers
        self.main_timer = self.create_timer(0.5, self.main_timer_callback)

    # Create callback methods (subscribers and timers)
    def callback_sub_LED(self, msg):
        self.estado_LED = msg.data
        GPIO.output(11,self.estado_LED)

    def callback_sub_servo(self, msg):
        pass

    def callback_sub_test(self,msg):
        self.get_logger().info(msg.data)

    # send info to actuators
    def main_timer_callback(self):
        self.estado_LED = not(self.estado_LED)
        GPIO.output(11,self.estado_LED)

    

def main(args=None) -> None:
    rclpy.init(args=args)
    node_name= NodeName()
    rclpy.spin(node_name)
    node_name.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)