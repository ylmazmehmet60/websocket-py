# WebSocket Project

This project demonstrates a WebSocket-based communication system with three key components:
1. **reader.py**: Acts as the WebSocket server, listening for incoming connections and handling messages.
2. **listen.py**: A WebSocket client that connects to the server and listens for messages.
3. **sender.py**: A WebSocket client responsible for sending messages to the server.

---

## **Setup and Deployment**

### **Prerequisites**
- Python 3.10 or higher
- Required Python libraries:
  - `websockets`
  - `asyncio`
- Internet access (for server and client communication)

### **Clone the Repository**
Clone the project repository from GitHub:
```bash
git clone https://github.com/ylmazmehmet60/websocket-py
cd websocket-py
```

## Install Dependencies

Install the required libraries:
```bash
pip install websockets==13.0 asyncio
```

## Expected Workflow
- **Server (reader.py):**
  1. Waits for incoming WebSocket connections on ```0.0.0.0:12345```.
  2. Logs messages received from clients.
     
- **Listener (listen.py):**
  1. Connects to the server and waits for messages.
  2. Displays messages sent by the server.
    
- **Sender (sender.py):**
  1. Connects to the server.
  2. Sends user-entered messages to the server.
 
## Figures

1. System Architecture
```bash
    +-------------+       +----------------+       +---------------+
    | sender.py   | --->  |  reader.py     | --->  |  listen.py    |
    | (WebSocket) |       | (WebSocket)    |       | (WebSocket)   |
    +-------------+       +----------------+       +---------------+
```

2. Communication Flow
```bash
    sender.py ---> reader.py ---> listen.py
       |                |              |
       +--- Echo -------+              |
                                       |
      <--- Message from server --------+
```

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
