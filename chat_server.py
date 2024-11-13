from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Handle a new connection
@socketio.on('connect')
def handle_connect():
    print("A user connected")

# Handle incoming messages
@socketio.on('message')
def handle_message(data):
    print("Received message:", data)
    # Broadcast the message to all connected clients
    send(data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=port)
