from machine import Pin, PWM # import the Pin and PWM modules from the machine library
from time import sleep # import the sleep module from the time library

# pin initialization
ENA = PWM(Pin(1)) # initialize PWM on pin 1 to control the left motor
IN1 = Pin(2,Pin.OUT) # pin 2 is used as an output to rotate the left motor direction forward
IN2 = Pin(3,Pin.OUT) # pin 3 is used as an output to rotate the left motor direction backwards
IN3 = Pin(4,Pin.OUT) # pin 4 is used as an output to rotate the right motor direction forward
IN4 = Pin(5,Pin.OUT) # pin 5 is used as an output to rotate the right motor direction backwards
ENB = PWM(Pin(6)) # initialize PWM on pin 6 to control the right motor
right = Pin(7, Pin.IN) # pin 7 is used as input in reading the value of the line sensor on the right side
middle = Pin(8, Pin.IN) # pin 8 is used as input in reading the value of the line sensor on the middle side
left = Pin(9, Pin.IN) # pin 9 is used as input in reading the value of the line sensor on the left side

# speed of this car robot
speed = 45000 # set the motor speed with a value of 45000 (in the range 0 - 65025)
ENA.duty_u16(speed) # set the PWM duty cycle for the left motor
ENB.duty_u16(speed) # set the PWM duty cycle for the right motor

# lineFollowing method
def lineFollowing():
    sleep(0.05) # 0.05 second delay
    return[left.value(),middle.value(),right.value()] # returns the value of the robot's line sensor in list form

# robot method
def robot():
    sensorValues = lineFollowing() # call the lineFollowing method
    if sensorValues == [1,1,1]:
        stop() # robot will stop
    elif sensorValues == [0,0,0]:
        stop() # robot will stop
    elif sensorValues == [1,0,1]:
        forward() # robot will move forward
    elif sensorValues == [0,1,1]:
        turnLeft() # robot will turn left
    elif sensorValues == [0,0,1]:
        turnLeft() # robot will turn left
    elif sensorValues == [1,1,0]:
        turnRight() # robot will turn right
    elif sensorValues == [1,0,0]:
        turnRight() # robot will turn right

# motor control method: forward
def forward():
    IN1.on()
    IN2.off() 
    IN3.on()
    IN4.off()

# motor control method: turn right
def turnRight():
    IN1.on()
    IN2.off()
    IN3.off()
    IN4.on()

# motor control method: turn left
def turnLeft():
    IN1.off()
    IN2.on()
    IN3.on()
    IN4.off()

# motor control method: stop
def stop():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()

# main method
if   __name__ == '__main__':
    try:
        # loop without stopping
        while True:
            robot() # this method applies robot movement logic based on the sensor values obtained from the lineFollowing method
          
    # exception handling
    except KeyboardInterrupt:
        stop() # robot is stopped by calling the stop() method
