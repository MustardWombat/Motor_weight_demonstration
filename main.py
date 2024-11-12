import time
import random

# Initial sensor IDs
id_0 = 0
id_1 = 0
id_6 = 0
id_7 = 0

def find_line(id_0, id_1, id_6, id_7, sensor_0, sensor_1, sensor_6, sensor_7):
    # Calculate difference based on sensor input
    if int(id_0) == 1 or int(id_1) == 1:
        diff = (0.25 * sensor_0 / 100) + (0.75 * sensor_1 / 100)
    elif int(id_6) == 1 or int(id_7) == 1:
        diff = (0.25 * sensor_6 / 100) + (0.75 * sensor_7 / 100 * 50)
    else:
        diff = 0  # Default if no line is detected
    return diff

while True:
    # Determine which sensors detect the line by random chance
    line_position = random.randint(0, 2)
    if line_position == 0:
        test_case = ("LINE RIGHT OF ROBOT\n"
                     "_________|")
        sensor_0 = random.randint(500, 1000)
        sensor_1 = random.randint(500, 1000)
        sensor_6 = random.randint(0, 500)
        sensor_7 = random.randint(0, 500)
    elif line_position == 1:
        test_case = ("LINE LEFT OF ROBOT\n"
                     "|_________")
        sensor_0 = random.randint(0, 500)
        sensor_1 = random.randint(0, 500)
        sensor_6 = random.randint(500, 1000)
        sensor_7 = random.randint(500, 1000)
    elif line_position == 2:
        test_case = ("LINE IS CENTERED\n"
                     "____|____")
        sensor_0 = 0
        sensor_1 = 0
        sensor_6 = 0
        sensor_7 = 0

    time.sleep(2)  # Simulate delay

    # Convert sensor values to binary detection (1 = line detected, 0 = no line)
    id_0 = 1 if sensor_0 < 500 else 0
    id_1 = 1 if sensor_1 < 500 else 0
    id_6 = 1 if sensor_6 < 500 else 0
    id_7 = 1 if sensor_7 < 500 else 0

    # Calculate velocity adjustment based on line detection
    velocity = find_line(id_0, id_1, id_6, id_7, sensor_0, sensor_1, sensor_6, sensor_7)

    # Ensure velocity stays within a maximum range to add up to 100%
    velocity = min(velocity, 50)  # Limits the added power to a maximum of 50%

    # Motor power adjustment based on velocity (50% to 100% range)
    if id_0 == 1 or id_1 == 1:
        motor_1 = 50 - velocity  # Front left motor
        motor_2 = 50 + velocity  # Front right motor
        motor_3 = 50 - velocity  # Back left motor
        motor_4 = 50 + velocity  # Back right motor
    elif id_6 == 1 or id_7 == 1:
        motor_1 = 50 + velocity  # Front left motor
        motor_2 = 50 - velocity  # Front right motor
        motor_3 = 50 + velocity  # Back left motor
        motor_4 = 50 - velocity  # Back right motor
    else:
        motor_1 = 50
        motor_2 = 50
        motor_3 = 50
        motor_4 = 50

    # Ensure motor power doesn't drop below 50% or exceed 100%
    motor_1 = max(min(motor_1, 99), 50)
    motor_2 = max(min(motor_2, 99), 50)
    motor_3 = max(min(motor_3, 99), 50)
    motor_4 = max(min(motor_4, 99), 50)

    # Print motor speeds and visual layout
    print(test_case)
    print(f"[{round(motor_1)}%]--[{round(motor_2)}%]\n"
          f"|        |\n"
          f"|        |\n"
          f"[{round(motor_3)}%]--[{round(motor_4)}%]\n")
