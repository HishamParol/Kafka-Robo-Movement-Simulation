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
  - Robot represented with a car icon (`car.png`).

---

## Project Structure

robot-simulation/ ├── robot_position/ │ ├── init.py # (optional for making this directory a package) │ ├── producer.py # Kafka producer to simulate robot movement │ └── requirements.txt # Python dependencies for producer ├── flask_app/ │ ├── templates/ │ │ └── index.html # Frontend template for the Flask app │ ├── static/ │ │ ├── car.png # Robot car icon │ │ └── styles.css # Custom styles for the Flask app │ ├── app.py # Flask app to consume Kafka data and serve it │ └── requirements.txt # Python dependencies for Flask app ├── .gitignore # Ignored files (e.g., virtual environment, logs, etc.) ├── README.md # Documentation for the project └── LICENSE # Project license

Copy
Edit


---

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

Step 2: Set Up Kafka Producer (Robot Movement Simulation)
Navigate to the robot_position/ directory:

bash
Copy
Edit
cd robot_position
Create a virtual environment and install dependencies:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
Update the Kafka broker address in producer.py:

python
Copy
Edit
KAFKA_BROKER = 'localhost:9092'
Run the Kafka producer:

bash
Copy
Edit
python producer.py
Step 3: Set Up Flask Application (Visualization)
Navigate to the flask_app/ directory:

bash
Copy
Edit
cd flask_app
Create a virtual environment and install dependencies:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
Update the Kafka broker address in app.py:

python
Copy
Edit
KAFKA_BROKER = 'localhost:9092'
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and navigate to:

arduino
Copy
Edit
http://localhost:5000
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



