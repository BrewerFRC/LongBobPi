import drive
import maestro
import xbox
import PiIO
import time

LEFT_MOTORS = 1
RIGHT_MOTORS = 0

j = xbox.Joystick()
motors = maestro.Controller()
drive = drive.DriveTrain(maestro, LEFT_MOTORS, RIGHT_MOTORS)
cannons = PiIO.Spike(4, 5)
arm = PiIO.Spike(6, 7)
leftLaunch = time.millis()
rightLaunch = time.millis()

while True:
    drive.drive(j.leftX(), j.leftY())

    #Add rising edge for triggers
    if j.whenRightTrigger() and rightLaunch < time.millis():
        rightLaunch = time.millis() + 500
    if time.millis() < rightLaunch:
        cannons.left(True)
    else:
        cannons.left(False)

    if j.whenLeftTrigger() and leftLaunch < time.millis():
        leftLaunch = time.millis() + 500
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
