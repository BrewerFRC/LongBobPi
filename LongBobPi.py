import drive
import maestro
import xbox
import PiIO
import time

#Motor pin IDs
LEFT_MOTORS = 1
RIGHT_MOTORS = 0
#The time to activate relays for cannon firing.
FIRE_TIME = 25

j = xbox.Joystick()
motors = maestro.Controller()
drive = drive.DriveTrain(maestro, LEFT_MOTORS, RIGHT_MOTORS)
cannons = PiIO.Spike(4, 5)
arm = PiIO.Spike(6, 7)
leftLaunch = time.millis()
rightLaunch = time.millis()

while True:
    drive.drive(j.leftX(), j.leftY())

    if j.whenRightTrigger() and rightLaunch < time.millis():
        rightLaunch = time.millis() + FIRE_TIME
    if time.millis() < rightLaunch:
        cannons.left(True)
    else:
        cannons.left(False)

    if j.whenLeftTrigger() and leftLaunch < time.millis():
        leftLaunch = time.millis() + FIRE_TIME
    if time.millis() < leftLaunch:
        cannons.right(True)
    else:
        cannons.right(False)

	if j.rightY() > 0.5:
		arm.forward()
	elif j.rightY() < -0.5:
		arm.reverse()
	else:
		arm.stop()
