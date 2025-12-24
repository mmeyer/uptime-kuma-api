#!/usr/bin/env python3
import socketio
import time
import sys

def setup_admin(username="admin", password="adminadmin!"):
    """
    Connect to Uptime Kuma via Socket.IO and send the setup message with admin credentials.
    """
    print(f"Setting up admin user: {username}")
    
    # Create a Socket.IO client
    sio = socketio.Client(logger=True)

    def setup_callback(data):
        if data and isinstance(data, dict):
            if data.get('ok'):
                print(f"Setup successful: {data.get('msg', 'No message')}")
            else:
                print(f"Setup failed: {data.get('msg', 'Unknown error')}")
        else:
            print(f"Received callback data: {data}")
    
    @sio.event
    def connect():
        print("Connected to Uptime Kuma WebSocket server")
        # Send the setup message with admin credentials
        sio.emit("setup", (username, password), callback=setup_callback)
        print("Setup message sent")
        # Wait a moment to ensure the message is processed
        time.sleep(5)
        # Disconnect after sending the message
        sio.disconnect()
    
    @sio.event
    def connect_error(data):
        print(f"Connection error: {data}")
        sys.exit(1)
    
    @sio.event
    def disconnect():
        print("Disconnected from Uptime Kuma WebSocket server")
    
    # Connect to the Socket.IO server
    try:
        sio.connect("ws://localhost:3001", transports=["websocket"])
        # Wait for the connection to complete
        sio.wait()
        return True
    except Exception as e:
        print(f"Error connecting to WebSocket server: {e}")
        return False

if __name__ == "__main__":
    # Allow custom username/password from command line arguments
    username = "admin"
    password = "secret123"
    
    if len(sys.argv) > 1:
        username = sys.argv[1]
    if len(sys.argv) > 2:
        password = sys.argv[2]
    
    success = setup_admin(username, password)
    if success:
        print(f"Setup process completed. Admin user '{username}' should be created if the server accepted the request.")
    sys.exit(0 if success else 1)
