# Robot Movement Simulation with Kafka and Flask

This project showcases a real-time simulation of a robot navigating through a 2D space filled with obstacles. The system is designed to demonstrate continuous tracking and visualization of the robot's movement while handling real-time data streaming. It uses Kafka to stream the robot's coordinates as it moves, and a Flask web application visualizes the robot's position and its movement history.

---

## Features

- **Real-Time Simulation**:
  - Robot's position updates dynamically on a 2D canvas.
  - Avoids obstacles and stays within canvas boundaries.

- **Kafka Integration**:
  - Kafka producer simulates robot movement and streams coordinates.
  - Flask app consumes Kafka messages for visualization.

- **Interactive Dashboard**:
  - Displays the robot's path, obstacles, and real-time position.
  - Obstacles box are drawn
  - Robot represented with a car icon (`car.png`).

---

## Project Structure
```bash
robot-simulation/

├── init.py # (optional for making this directory a package) │
├── requirements.txt│
├── robot_position.py │
├── app.py  │
├── templates/ 
    └── index.html │
├── static/  
    └── car.png  │
├── README.md 

```


## Kafka for Real-Time Streaming

- Kafka acts as the central data pipeline, allowing the robot's position updates to be streamed in real time.
- A producer script generates and sends the robot's coordinates to a Kafka topic.
- A consumer (Flask app) reads these updates and processes them for visualization.
  
## Flask Web Application for Visualization

- The Flask app continuously consumes data from Kafka.
- It renders a visual board that displays the robot's current position, movement path, and obstacles.
- The robot is represented by a car icon, and the UI updates in real time.
  
## Robot Movement and Collision Handling

- The robot moves within a predefined 2D grid or canvas.
- When it collides with a boundary or an obstacle, it detects the collision and changes direction accordingly.
- This behavior mimics an autonomous navigation system with basic obstacle avoidance.

---

## Setup and Installation

### Prerequisites

- **Python** (>= 3.8)
- **Kafka Broker** (Running locally or in the cloud)
- **Confluent Kafka Python Library** (`confluent-kafka`)

---

### Step 1: Install Kafka
- Refer to this document for downloading Kafka locally

### Step 2: Clone the Repository

```bash
git gh repo clone HishamParol/Kafka-Robo-Movement-Simulation
cd Kafka-Robo-Movement-Simulation
```
### Step 3: Setup Kafka on the Local Computer
- Once you download the Kafka in your local computer
- Go to kafka folder ~/kafka_2.13-3.9.0
- Go to Server properties \config\server
#### Configure Kafka Broker
```bash
broker.id=1
log.dirs=/var/lib/kafka/data
num.partitions=3
log.retention.hours=168
default.replication.factor=2
zookeeper.connect=localhost:9092
```
#### Start Kafka Broker and Zookeeper
- Open a new Terminal
- Start the Zookeeper
  
```bash
  cd ~\kafka_2.13-3.9.0 (kafka folder)
 .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```
- Open another Terminal
- Start the Kafka Broker
```bash
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

### Step 4: Setup the Environment
- Open a new Terminal
- Navigate to the Project directory:
- Create a virtual environment and install dependencies:
```bash
cd 'Project Folder'
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```
### Step 5: Run the Robot Simulation Producer code
- Set the KAFKA_BROKER in the producer code (robot_position.py)
```bash
KAFKA_BROKER = 'localhost:9092'
```

- Run the Producer code
  
```bash
python robot_position.py
```
### Step 5: Run the Main Flask App

- In the new Terminal
```bash
python app.py
```
- The Flask app will retrieve data from the Kafka topics produced by the producer code.
- The Flask app will display a visual board that shows the real-time movement of the robots.
- The robot is represented by a car icon.
- If a robot collides with a boundary or obstacle, it will change direction
- Open your browser and navigate to the port provided

---

## Key Features
- ✔ Real-Time Data Processing → Kafka enables fast and efficient streaming of movement data.
- ✔ Dynamic Visualization → Flask updates the UI as new data arrives.
- ✔ Obstacle Handling → The robot intelligently detects and reacts to collisions.
- ✔ Scalability → Kafka allows multiple robots to be tracked simultaneously.
