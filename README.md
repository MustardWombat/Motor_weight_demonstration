# Line Detection and Velocity-Based Motor Control

## Project Description
This Python program simulates a simple line-following robot with sensors and motor adjustments based on line detection. The program uses **random sensor values** to simulate real-world conditions and determines the robot's motor velocity adjustments to keep it aligned with the detected line. It incorporates basic principles of robotics and sensor data processing while introducing key Python programming concepts.

---

## Key Features
1. **Line Detection**:
   - Uses random sensor inputs to simulate line position (`left`, `right`, `centered`).
   - Converts sensor data into binary detections (line detected: `1`, no line: `0`).

2. **Dynamic Velocity Adjustment**:
   - Calculates velocity adjustments based on the line's position relative to the robot using the `find_line()` function.
   - Limits velocity changes to maintain motor power in a safe range.

3. **Motor Control**:
   - Adjusts motor power (front and back motors) based on the line's position and velocity calculations.
   - Ensures motor power stays between 50% and 100%.

4. **Visual Feedback**:
   - Provides a visual representation of the line position (`left`, `right`, or `centered`) and motor power distribution.

5. **Error Handling**:
   - Simulates delays and random scenarios to ensure robust handling of dynamic input conditions.

---

## How It Works
1. **Random Line Position**:
   - Simulates whether the line is to the **left**, **right**, or **centered** relative to the robot.
   - Random sensor values are generated to reflect these positions.

2. **Sensor Binary Conversion**:
   - Sensors `0, 1, 6, 7` detect the line. If sensor values are below a threshold (`500`), they register as `1` (line detected).

3. **Velocity Calculation**:
   - Uses a weighted formula to adjust velocity based on detected sensor inputs.

4. **Motor Power Adjustment**:
   - Adjusts motor speeds to steer the robot toward the line, ensuring balanced movement and maintaining motor power limits.

5. **Output**:
   - Prints the simulated line position and motor power distribution for each loop iteration.

---

## Program Elements
1. **Python Concepts**:
   - References
   - Loops
   - Functions
   - Conditional Statements (e.g., `if`, `elif`, `else`)
   - String Manipulation
   - Constants and Variables
   - Error Handling

2. **Libraries Used**:
   - `time`: Simulates a delay between sensor readings.
   - `random`: Generates random sensor inputs to mimic real-world scenarios.

3. **Functionality**:
   - `find_line()`: Calculates the velocity adjustment based on sensor data.
   - Motor adjustment logic ensures smooth and safe robot movement.

---

## Sample Output

### Example: Line Right of Robot
LINE RIGHT OF ROBOT
_________|

[50%]--[70%]
|        |
|        |
[50%]--[70%]

### Example: Line Left of Robot
LINE LEFT OF ROBOT
|_________

[70%]--[50%]
|        |
|        |
[70%]--[50%]

### Example: Line Centered
LINE IS CENTERED
____|____

[50%]--[50%]
|        |
|        |
[50%]--[50%]

---

## How to Run
1. Ensure Python 3.x is installed.
2. Save the code in a file named `line_detection_sim.py`.
3. Run the program in a terminal or Python IDE:
   ```bash
   python line_detection_sim.py
