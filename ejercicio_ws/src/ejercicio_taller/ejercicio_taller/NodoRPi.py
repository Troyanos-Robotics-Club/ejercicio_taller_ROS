import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String
import time

class NodoRPi(Node):
    def __init__(self) -> None:
        super().__init__('NodoRPi')

        # pins setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT) #LED
        GPIO.setup(13,GPIO.OUT) #PWM al servo 
        GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Boton
        GPIO.setup(40,GPIO.OUT) #TRIG sonic sensor - output
        GPIO.setup(38,GPIO.IN)  #ECHO sonic sensor - input

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
        self.estado_boton_anterior = False
        self.pwm_servo = 7.5
        self.servo = GPIO.PWM(13,50)
        self.servo.start(self.pwm_servo)

        # Create timers
        self.main_timer = self.create_timer(0.1, self.main_timer_callback)

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
        # Manejo del boton
        self.estado_boton = GPIO.input(37)
        if (self.estado_boton and not(self.estado_boton_anterior)):
            self.publisher_boton.publish(True)
        if (GPIO.input(37)): self.estado_boton_anterior = True
        else: self.estado_boton_anterior = False

        #Manejo del sensor ultrasonico
        # Lanza pulso del trig
        GPIO.output(40,True)
        time.sleep(0.00001)
        GPIO.output(40,False)
        while (not(GPIO.input(38))): pulse_start = time.time()
        while (GPIO.input(38)): pulse_end = time.time()
        pulse_dur = pulse_end - pulse_start
        self.distancia_sensor = pulse_dur*34300/2

        # Prints de output test 
        self.get_logger().info(str(self.distancia_sensor))
        self.estado_LED = not(self.estado_LED)
        GPIO.output(11,self.estado_LED)

def main(args=None) -> None:
    rclpy.init(args=args)
    nodo = NodoRPi()
    rclpy.spin(nodo)
    GPIO.cleanup()
    nodo.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)