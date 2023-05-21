#Import necessary libraries
import RPi.GPIO as GPIO
import time


# Set up GPIO pins
'''
We specify the GPIO pins used for the proximity sensor and the light.

sensor_pin is set as an input pin,
indicating it will be used to read the status of the proximity sensor.

light_pin is set as an output pin,
indicating it will control the light.
'''


sensor_pin = 18  # The GPIO pin connected to the proximity sensor
light_pin = 17   # The GPIO pin connected to the light

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(light_pin, GPIO.OUT)


while True:
    if GPIO.input(sensor_pin):  # If the sensor detects someone
        GPIO.output(light_pin, GPIO.HIGH)  # Turn on the light
        print("Person detected. Light turned on for 10s.")
        time.sleep(10) #Time delay for the light to be on for if a person is detected 
    else:
        GPIO.output(light_pin, GPIO.LOW)  # Turn off the light
        print("No person detected. Light turned off.")
        time.sleep(0.1)  # Pause for a short duration to avoid excessive readings

