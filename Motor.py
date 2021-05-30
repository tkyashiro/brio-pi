from __future__ import print_function
import RPi.GPIO as GPIO
import time
import sys

class Motor(object):
    MOTOR_SPEED_MAX = 5
    MOTOR_SPEED_STOP = 0
    MOTOR_SPEED_MIN = -5
    
    current_speed = MOTOR_SPEED_STOP

    pwm0 = None
    pwm1 = None

    def __init__(self):
        self.setup()
    
    def setup(self):
        pin_pwm0 = 32
        pin_pwm1 = 33
    
        GPIO.setmode(GPIO.BOARD)
    
        GPIO.setup(pin_pwm0, GPIO.OUT)
        GPIO.setup(pin_pwm1, GPIO.OUT)
    
        self.pwm0 = GPIO.PWM(pin_pwm0, 3000)
        self.pwm1 = GPIO.PWM(pin_pwm1, 3000)
    
        self.pwm0.start(00)
        self.pwm1.start(00)

    def __del__(self):
        self.teardown()
    
    def teardown(self):
        GPIO.cleanup()

    def currentSpeed(self):
        return self.current_speed
    
    def changeSpeed(self, direction_and_speed):
        if (direction_and_speed > self.MOTOR_SPEED_MAX):
            # do nothing
            return 0
        elif (direction_and_speed < self.MOTOR_SPEED_MIN):
            # do nothing
            return 0
    
        if (direction_and_speed * self.current_speed <= 0):
            # Stop both when you have to change direction
            self.pwm0.ChangeDutyCycle(0)
            self.pwm1.ChangeDutyCycle(0)
            time.sleep(2.0)
    
        # Limit the voltage to the DC motor to 3V, 
        # where the input Vcc is 5V 
        max_duty = 100 * 3.0 / 5.0 
    
        if (direction_and_speed > 0):
            duty = max_duty * direction_and_speed / self.MOTOR_SPEED_MAX
            self.pwm0.ChangeDutyCycle(duty)
            print ("PWM0 duty : {0}".format(duty), file=sys.stderr)
        elif (direction_and_speed < 0):
            duty = max_duty * direction_and_speed / self.MOTOR_SPEED_MIN
            self.pwm1.ChangeDutyCycle(duty)
            print ("PWM1 duty : {0}".format(duty), file=sys.stderr)

        self.current_speed = direction_and_speed
        sys.stderr.flush()
        return self.current_speed
    
    
