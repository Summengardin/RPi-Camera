import time
from sparkfun_servophat import Sparkfun_Servo_Phat

# Create an instance of the Servo Phat
servo_phat = Sparkfun_Servo_Phat()

def move_servo(port, position):
    """
    Move a servo connected to a specified port to a specified position.

    :param port: The port number where the servo is connected.
    :param position: Position to move the servo, generally between 0 and 180.
    """
    servo_phat.move_servo_position(port, position, 180)

try:
    while True:
        # Move servo on port 0 to 90 degrees
        move_servo(0, 60)
        # Move servo on port 1 to 90 degrees
        move_servo(1, 60)

        # Wait for 1 second
        time.sleep(1)

        # Move servo on port 0 to 0 degrees
        move_servo(0, 70)
        # Move servo on port 1 to 0 degrees
        move_servo(1, 70)

        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Ensure the PWM outputs are off before exiting
    servo_phat.disable_servo(0)
    servo_phat.disable_servo(1)
