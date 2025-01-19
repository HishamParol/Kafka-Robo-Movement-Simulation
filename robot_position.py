import time
import random
import json
from confluent_kafka import Producer

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'  # Update this with your Kafka broker
KAFKA_TOPIC = 'robotposition'   # The Kafka topic to send data to

# Initialize Kafka producer
conf = {
    'bootstrap.servers': KAFKA_BROKER,
}

producer = Producer(conf)

# Robot's initial position and velocity
robot_data = {"x": 50, "y": 50, "vx": 3, "vy": 3}

# Obstacles (simulating rough terrain with irregular shapes and sizes)
obstacles = [
    {"x": 200, "y": 100, "width": 120, "height": 50, "type": "rock"},
    {"x": 400, "y": 250, "width": 150, "height": 100, "type": "boulder"},
    {"x": 600, "y": 400, "width": 80, "height": 80, "type": "mud"},
    {"x": 100, "y": 450, "width": 150, "height": 70, "type": "rough_ground"},
    {"x": 300, "y": 50, "width": 50, "height": 50, "type": "pothole"},
    {"x": 500, "y": 300, "width": 120, "height": 40, "type": "rough_ground"},
]

# Path storage to track the entire journey
robot_path = [{"x": robot_data["x"], "y": robot_data["y"]}]  # Start with initial position

# Function to generate a random direction
def random_direction():
    return random.choice([-3, -2, -1, 1, 2, 3])

# Check if the robot collides with an obstacle
def is_collision(x, y):
    for obstacle in obstacles:
        if (
            obstacle["x"] <= x <= obstacle["x"] + obstacle["width"]
            and obstacle["y"] <= y <= obstacle["y"] + obstacle["height"]
        ):
            return True
    return False

# Callback for Kafka producer to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for message {msg.key()}: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Function to simulate the robot's movement and send coordinates to Kafka
def simulate_robot():
    global robot_data
    while True:
        # Update the robot's position
        robot_data["x"] += robot_data["vx"]
        robot_data["y"] += robot_data["vy"]

        # Ensure the robot doesn't go out of the canvas
        if robot_data["x"] <= 0 or robot_data["x"] >= 800:
            robot_data["vx"] = random_direction()
        if robot_data["y"] <= 0 or robot_data["y"] >= 600:
            robot_data["vy"] = random_direction()

        # Check for obstacle collisions
        if is_collision(robot_data["x"], robot_data["y"]):
            robot_data["vx"] = random_direction()
            robot_data["vy"] = random_direction()

        # Add the current position to the path
        robot_path.append({"x": robot_data["x"], "y": robot_data["y"]})

        # Send the robot's current position to Kafka
        producer.produce(KAFKA_TOPIC, key=str(robot_data["x"]) + "," + str(robot_data["y"]), value=json.dumps(robot_data), callback=delivery_report)
        
        # Ensure delivery of the message
        producer.poll(0)

        # Pause to slow down the robot (half a second)
        time.sleep(1)

if __name__ == "__main__":
    simulate_robot()
