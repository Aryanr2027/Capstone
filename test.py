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
