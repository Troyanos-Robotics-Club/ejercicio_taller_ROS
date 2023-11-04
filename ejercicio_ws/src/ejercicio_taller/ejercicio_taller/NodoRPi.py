import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String

class NodeName(Node):
    def __init__(self) -> None:
        super().__init__('node_name')

        # pins setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT) #LED
        GPIO.setup(13,GPIO.OUT) #PWM al servo 
        GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Boton
        GPIO.add_event_detect(15,GPIO.RISING, callback=self.callback_boton)

        # Create Publishers
        self.publisher_proxomidad = self.create_publisher(Float32, "/distancia_sensor",10)
        self.publisher_boton = self.create_publisher(Bool, "/estado_boton",10)

        # Create Subscribers
        self.subscriber_LED = self.create_subscription(Bool,"/estado_LED",self.callback_sub_LED,10)
        self.subscriber_servo = self.create_subscription(Float32,"/pwm_servo", self.callback_sub_servo,10)

        self.subscriber_test = self.create_subscription(String,"/topic_test",self.callback_sub_test,10)

        # Initialize attributes
        self.estado_LED = True
        self.distancia_sensor = 0.0
        self.estado_boton = False
        self.pwm_servo = 7.5
        self.servo = GPIO.PWM(13,50)
        self.servo.start(self.pwm_servo)

        # Create timers
        self.main_timer = self.create_timer(0.01, self.main_timer_callback)

    # Create callback methods (subscribers and timers)
    def callback_sub_LED(self, msg):
        self.estado_LED = msg.data
        GPIO.output(11,self.estado_LED)

    def callback_sub_servo(self, msg):
        self.pwm_servo = msg.data
        self.sevo.ChangeDutyCycle(self.pwm_servo)

    def callback_sub_test(self,msg):
        self.get_logger().info(msg.data)

    def main_timer_callback(self): #publicar info de los sensores 
        pass

    def callback_boton(self):
        self.get_logger().info("lo presiono")
        

def main(args=None) -> None:
    rclpy.init(args=args)
    node_name= NodeName()
    rclpy.spin(node_name)
    GPIO.cleanup()
    node_name.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)