import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

print("turning on and off led")

try:
	while True:
		GPIO.output(LED_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_PIN, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	print("Exiting")
finally:
	GPIO.cleanup()
