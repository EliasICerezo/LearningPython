import RPi.GPIO as GPIO
from subprocess import call
GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN)

#GPIO.setup(14, GPIO.OUT)
#GPIO.output(14, True)

GPIO.wait_for_edge(3, GPIO.FALLING)

call(['sudo', 'shutdown', '-h', 'now'], shell=False)
