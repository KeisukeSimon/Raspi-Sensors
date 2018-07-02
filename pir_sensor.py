import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led1 = 4
pirPin = 6

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(pirPin,GPIO.IN)

#def LIGHT(pirPin):
#	print("Motion Detected")
#	print("Lights on")
#	GPIO.output(led1,GPIO.HIGH)

#	time.sleep(2)

#	GPIO.output(led1,GPIO.LOW)

print ("Motion Sensor Alarm")
time.sleep(.2)
print("ready")

try:
	while True:
		if (GPIO.input(pirPin)):
			print("Motion Detected")
			GPIO.output(led1,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(led1,GPIO.LOW)

#	GPIO.add_event_detect(pirPin, GPIO.RISING, callback=LIGHT)
#	while 1:
#		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
