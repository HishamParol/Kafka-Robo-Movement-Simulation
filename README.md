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
├── templates/ │
    └── index.html │
├── static/ │ 
    └── car.png  │
├── README.md 

```

## Setup and Installation

### Prerequisites

- **Python** (>= 3.8)
- **Kafka Broker** (Running locally or in the cloud)
- **Confluent Kafka Python Library** (`confluent-kafka`)

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/robot-simulation.git
cd robot-simulation
```
###Step 2: Set Up Kafka Producer (Robot Movement Simulation)
Navigate to the robot_position/ directory:

```bash
cd robot_position
Create a virtual environment and install dependencies:
```

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
Update the Kafka broker address in producer.py:
```

python
```bash
KAFKA_BROKER = 'localhost:9092'
Run the Kafka producer:
```

```bash
python producer.py
Step 3: Set Up Flask Application (Visualization)
Navigate to the flask_app/ directory:
```

```bash
cd flask_app
Create a virtual environment and install dependencies:
```

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
Update the Kafka broker address in app.py:
```

```bash
KAFKA_BROKER = 'localhost:9092'
Run the Flask app:
```

```bash
python app.py
Open your browser and navigate to:
```

arduino
```bash
http://localhost:5000
```
How It Works
Producer:

Simulates a robot navigating through a 2D space.
Streams the robot's x, y coordinates to Kafka.
Consumer (Flask App):

Consumes the robot's position data from Kafka in real-time.
Renders the data on a 2D canvas.
Visualization:

Robot's position is represented by a car icon (car.png).
Obstacles are visualized on the canvas.
Full path of the robot's movement is preserved.
Example Visualization
Feature	Example Screenshot
Robot Movement	
Real-Time Data	Shows last 10 positions in a side panel.
Obstacle Handling	Robot navigates around obstacles.



