from machine import Pin, PWM # import the Pin and PWM modules from the machine library
from utime import sleep # import the sleep module from the time library

# setup method
def setup():
    # global variable
    global ENA, IN1, IN2, IN3, IN4, ENB, speed, right, middle, left
    
    # motor dc initialization
    ENA = PWM(Pin(1)) # initialize PWM on pin 1 to control the left motor
    IN1 = Pin(2, Pin.OUT) # pin 2 is used as an output to rotate the left motor direction backwards
    IN2 = Pin(3, Pin.OUT) # pin 3 is used as an output to rotate the left motor direction forward
    IN3 = Pin(4, Pin.OUT) # pin 4 is used as an output to rotate the right motor direction forward
    IN4 = Pin(5, Pin.OUT) # pin 5 is used as an output to rotate the right motor direction backwards
    ENB = PWM(Pin(6)) # initialize PWM on pin 6 to control the right motor
    
    # speed of this car robot
    speed = 45000 # set the motor speed with a value of 45000 (in the range 0 - 65025)
    ENA.duty_u16(speed) # set the PWM duty cycle for the left motor
    ENB.duty_u16(speed) # set the PWM duty cycle for the right motor
    ENA.freq(1000) # ENA pin PWM frequency set to 1000 Hz
    ENB.freq(1000) # ENB pin PWM frequency set to 1000 Hz
    
    # sensor initialization
    right = Pin(7, Pin.IN) # pin 7 is used as input in reading the value of the line sensor on the right side
    middle = Pin(8, Pin.IN) # pin 8 is used as input in reading the value of the line sensor on the middle side
    left = Pin(9, Pin.IN) # pin 9 is used as input in reading the value of the line sensor on the left side

# loop method
def loop():
    while True:
        sensorValues = lineFollowing() # call the lineFollowing method
        if sensorValues == [1,1,1]: # sensor value -> left, middle, right = 1 (detected)
            stop() # robot will stop
        elif sensorValues == [0,0,0]: # sensor value -> left, middle, right = 0 (not detected)
            stop() # robot will stop
        elif sensorValues == [1,0,1]: # sensor value -> left & right = 1 (detected), middle = 0 (not detected)
            forward() # robot will move forward
        elif sensorValues == [0,1,1]: # sensor value -> right & middle = 1 (detected), left = 0 (not detected)
            turnLeft() # robot will turn left
        elif sensorValues == [0,0,1]: # sensor value -> right = 1 (detected), middle & left = 0 (not detected)
            turnLeft() # robot will turn left
        elif sensorValues == [1,1,0]: # sensor value -> middle & left = 1 (detected), right = 0 (not detected)
            turnRight() # robot will turn right
        elif sensorValues == [1,0,0]: # sensor value -> left = 1 (detected), middle & right = 0 (not detected)
            turnRight() # robot will turn right

# lineFollowing method
def lineFollowing():
    sleep(0.05) # 0.05 second delay
    return[left.value(),middle.value(),right.value()] # returns the value of the robot's line sensor

# motor control method: forward
def forward():
    print("forward")
    IN1.low()
    IN2.high() 
    IN3.high()
    IN4.low()

# motor control method: turn right
def turnRight():
    print("turn right")
    IN1.low()
    IN2.high() 
    IN3.low()
    IN4.high()

# motor control method: turn left
def turnLeft():
    print("turn left")
    IN1.high()
    IN2.low() 
    IN3.high()
    IN4.low()

# motor control method: stop
def stop():
    print("stop")
    IN1.low()
    IN2.low()
    IN3.low()
    IN4.low()

# main method
if __name__ == '__main__':
    try:
        setup() # calling the setup() method
        loop() # calling the loop() method
          
    except KeyboardInterrupt:
        stop() # robot is stopped by calling the stop() method
