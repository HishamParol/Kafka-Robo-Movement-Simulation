# Robot Movement Simulation with Kafka and Flask

This project demonstrates a real-time simulation of a robot navigating through a 2D space with obstacles. It uses Kafka to stream the robot's coordinates as it moves, and a Flask web application visualizes the robot's position and its movement history.

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

## Setup and Installation

### Prerequisites

- **Python** (>= 3.8)
- **Kafka Broker** (Running locally or in the cloud)
- **Confluent Kafka Python Library** (`confluent-kafka`)

### Step 1: Install Kafka
- Refer to this document for downloading Kafka locally

### Step 2: Clone the Repository

```bash
git clone https://github.com/<your-username>/robot-simulation.git
cd robot-simulation
```
### Step 3: Setup Kafka on the Local Computer
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
- Navigate to the robot_position/ directory:
- Create a virtual environment and install dependencies:
```bash
cd robot_position
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```
### Step 5: Run the Robot Simulation Producer code
- Set the KAFKA_BROKER in the producer code
```bash
KAFKA_BROKER = 'localhost:9092'
```

- Run producer.py code
  
```bash
python producer.py
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

