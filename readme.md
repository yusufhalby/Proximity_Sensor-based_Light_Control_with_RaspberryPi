# Proximity Sensor-based Light Control with Raspberry Pi

## Description
This Python code enables the control of a light using a proximity sensor connected to a Raspberry Pi. The program continuously monitors the sensor's input and toggles the light accordingly. When the proximity sensor detects a person's presence, the light turns on, and when no person is detected, the light turns off.

## Prerequisites
- Raspberry Pi with RPi.GPIO library installed
- Proximity sensor connected to a GPIO pin on the Raspberry Pi
- Light connected to another GPIO pin on the Raspberry Pi

## Imported Libraries
- RPi.GPIO: Provides access to the Raspberry Pi's GPIO pins for input and output control.
- time: Enables the introduction of delays in the code.

## Configuration
1. Define the GPIO pins for the proximity sensor and the light:
   - `sensor_pin`: GPIO pin connected to the proximity sensor (input pin).
   - `light_pin`: GPIO pin connected to the light (output pin).

## Main Code
The code is structured as follows:

1. Set up GPIO pins:
   - Configure the Raspberry Pi's GPIO mode and set the `sensor_pin` and `light_pin` as input and output pins, respectively, using the `GPIO.setup()` function.

2. Continuous monitoring and light control:
   - Enter an infinite loop using the `while True` statement to continuously monitor the proximity sensor and control the light.
   - Check the status of the proximity sensor using the `GPIO.input()` function.
   - If the sensor detects a person (`GPIO.input(sensor_pin)` returns True), perform the following steps:
     - Turn on the light by setting the `light_pin` to HIGH using `GPIO.output(light_pin, GPIO.HIGH)`.
     - Print a message indicating that a person is detected and the light is turned on.
     - Introduce a time delay of 10 seconds using `time.sleep(10)` to keep the light on for that duration.
   - If the sensor does not detect a person, perform the following steps:
     - Turn off the light by setting the `light_pin` to LOW using `GPIO.output(light_pin, GPIO.LOW)`.
     - Print a message indicating that no person is detected and the light is turned off.
     - Introduce a short time delay of 0.1 seconds using `time.sleep(0.1)` before checking the sensor's status again.

## Cleaning Up
- The code does not explicitly handle cleanup, such as cleaning up the GPIO pins, as it assumes that the program will run indefinitely. However, it is good practice to include `GPIO.cleanup()` at the end of the code or in exception handlers to release any resources used by the GPIO library and reset the GPIO pins when the program terminates.

## Usage
1. Connect the proximity sensor and the light to the appropriate GPIO pins on the Raspberry Pi.
2. Run the Python script using a Python interpreter on the Raspberry Pi.
3. Observe the output messages in the console, indicating the detection and status of the proximity sensor and the light control.

**Note**: Ensure that the RPi.GPIO library is installed on your Raspberry Pi. You can install it using pip: `pip install RPi.GPIO`.
Make sure to adjust the `sensor_pin` and `light_pin` values according to the GPIO pins you are using for the proximity sensor and the light.
