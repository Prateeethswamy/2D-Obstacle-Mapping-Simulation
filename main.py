import cv2
import numpy as np
import math
import random

# Window settings
WIDTH = 800
HEIGHT = 600

# Sensor settings
SENSOR_RANGE = 250
DETECTION_THRESHOLD = 120
SENSOR_ANGLE = 40  # degrees

# Robot position (fixed at bottom center)
robot_x = WIDTH // 2
robot_y = HEIGHT - 80

# Simulated object
object_x = random.randint(100, WIDTH - 100)
object_y = 100

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_within_sensor_cone(obj_x, obj_y):
    dx = obj_x - robot_x
    dy = robot_y - obj_y

    angle = math.degrees(math.atan2(dx, dy))
    distance = calculate_distance(robot_x, robot_y, obj_x, obj_y)

    if abs(angle) <= SENSOR_ANGLE and distance <= SENSOR_RANGE:
        return True, distance
    return False, distance

while True:
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Draw robot
    cv2.circle(frame, (robot_x, robot_y), 20, (255, 255, 255), -1)

    # Draw sensor cone
    for angle in range(-SENSOR_ANGLE, SENSOR_ANGLE + 1, 2):
        rad = math.radians(angle)
        end_x = int(robot_x + SENSOR_RANGE * math.sin(rad))
        end_y = int(robot_y - SENSOR_RANGE * math.cos(rad))
        cv2.line(frame, (robot_x, robot_y), (end_x, end_y), (50, 50, 50), 1)

    # Move object downward
    object_y += 2
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(100, WIDTH - 100)

    # Draw object
    cv2.circle(frame, (object_x, object_y), 15, (0, 255, 0), -1)

    # Detection logic
    detected, distance = is_within_sensor_cone(object_x, object_y)

    if detected and distance <= DETECTION_THRESHOLD:
        cv2.putText(frame, "OBJECT DETECTED!", (250, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(frame, f"Distance: {int(distance)} px", (280, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    else:
        cv2.putText(frame, "Scanning...", (320, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Ultrasonic Object Detection Simulation", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

