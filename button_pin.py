import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led=4
button=18

GPIO.setup(led,GPIO.OUT)
GPIO.setup(button,GPIO.IN)


try:
	while True:
		if not(GPIO.input(button)):
			print("Button pressed")
			GPIO.output(led,GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(led,GPIO.LOW)

except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
