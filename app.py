from flask import Flask, render_template, Response
from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import threading

app = Flask(__name__)

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'  # Update this with your Kafka broker
KAFKA_TOPIC = 'robotposition'

# Initialize Kafka consumer
conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'robot-consumer-group',
    'auto.offset.reset': 'earliest',  # Start consuming from the earliest message
}

consumer = Consumer(conf)

# Obstacles (simulating rough terrain with irregular shapes and sizes)
obstacles = [
    {"x": 200, "y": 100, "width": 120, "height": 50, "type": "rock"},
    {"x": 400, "y": 250, "width": 150, "height": 100, "type": "boulder"},
    {"x": 600, "y": 400, "width": 80, "height": 80, "type": "mud"},
    {"x": 100, "y": 450, "width": 150, "height": 70, "type": "rough_ground"},
    {"x": 300, "y": 50, "width": 50, "height": 50, "type": "pothole"},
    {"x": 500, "y": 300, "width": 120, "height": 40, "type": "rough_ground"},
]

# Flask route for the main page
@app.route("/")
def index():
    return render_template("index.html", obstacles=obstacles)

# Flask route to stream the robot's data from Kafka
@app.route("/data_stream")
def data_stream():
    def generate():
        while True:
            msg = consumer.poll(timeout=1.0)  # Poll Kafka with a timeout
            print('This is message:', msg)
            if msg is None:
                continue  # No message available yet, continue polling
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition reached
                    print(f"End of partition reached {msg.partition}")
                else:
                    # Handle other errors
                    raise KafkaException(msg.error())
            else:
                # Valid message, send it to the frontend
                data = msg.value().decode('utf-8')  # Decode bytes to string
                yield f"data:{data}\n\n"

    return Response(generate(), mimetype="text/event-stream")

# Function to start Kafka consumer in a separate thread
def start_kafka_consumer():
    consumer.subscribe([KAFKA_TOPIC])
    try:
        while True:
            consumer.poll(1.0)
              # Poll for messages
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()  # Always close the consumer when done

# Start the Kafka consumer in a background thread
threading.Thread(target=start_kafka_consumer, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
