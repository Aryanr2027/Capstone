import RPi.GPIO as GPIO
import time

# Set GPIO mode to GPIO.BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the sensor
TRIG = 23
ECHO = 24

# Set up the GPIO channels - one input, one output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Ensure the trigger pin is low for a brief period to settle the sensor
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    # Send a 10us pulse to start the measurement
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Initialize the start and stop times
    start_time = time.time()
    stop_time = time.time()

    # Record the start time while the ECHO pin is low (waiting for the pulse)
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Record the arrival time when the ECHO pin goes high
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Calculate the distance based on the time difference and speed of sound
    # Speed of sound = 34300 cm/s, divided by 2 for the round trip
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()







import RPi.GPIO as GPIO
import time

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Define the pin number for the sensor's output
sensor_pin = 17

# Set up the sensor pin as an input
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        # Read from the sensor
        if GPIO.input(sensor_pin) == 0:
            print("Obstacle detected!")
        else:
            print("Path is clear.")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Program exited by user")

finally:
    # Clean up the GPIO pins to reset them back to input mode
    GPIO.cleanup()








import RPi.GPIO as GPIO
import time

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Define the pin numbers for the sensors' outputs
sensors = {
    'Sensor 1': 17,
    'Sensor 2': 27,
    'Sensor 3': 22,
    'Sensor 4': 23
}

# Set up each sensor pin as an input
for sensor, pin in sensors.items():
    GPIO.setup(pin, GPIO.IN)

def check_obstacles():
    for sensor, pin in sensors.items():
        if GPIO.input(pin) == 0:  # Obstacle detected
            print(f"{sensor} detected an obstacle!")
        else:
            print(f"{sensor} path is clear.")

try:
    while True:
        check_obstacles()
        time.sleep(1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    print("Program exited by user")

finally:
    GPIO.cleanup()  # Reset the GPIO pins to their default state

