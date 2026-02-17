import random
import cv2
import numpy as np

class Environment:
    def __init__(self, width, height, num_obstacles=5):
        self.width = width
        self.height = height
        self.num_obstacles = num_obstacles
        self.obstacles = self.generate_obstacles()

    def generate_obstacles(self):
        obstacles = []
        for _ in range(self.num_obstacles):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 200)
            radius = random.randint(15, 30)
            obstacles.append((x, y, radius))
        return obstacles
    
    def draw(self, frame):
        # Draw boundary
        cv2.rectangle(frame, (0, 0), (self.width - 1, self.height - 1), (255, 255, 255), 2)
        # Draw obstacles
        for (x, y, r) in self.obstacles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), -1)

    def get_obstacles(self):
        return self.obstacles

