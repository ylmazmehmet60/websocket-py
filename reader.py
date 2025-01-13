import asyncio
import websockets

# Define the valid token
VALID_TOKEN = "secure-token-123"

connected_listeners = set()  # Store all listener connections

async def handler(websocket, path):
    # Validate the token
    token = websocket.request_headers.get("Sec-WebSocket-Protocol")
    if token != VALID_TOKEN:
        print("Invalid token. Closing connection.")
        await websocket.close(reason="Unauthorized")
        return

    # Add the websocket to the listener set
    connected_listeners.add(websocket)
    print("New client connected.")
    
    try:
        async for message in websocket:
            print(f"Server 1 received: {message}")
            # Broadcast the message to all connected listeners
            for listener in connected_listeners:
                if listener != websocket:
                    await listener.send(message)
    except websockets.ConnectionClosed:
        print("Client disconnected.")
    finally:
        connected_listeners.remove(websocket)

async def main():
    server = await websockets.serve(handler, "localhost", 12345)
    print("Server 1 is running on ws://localhost:12345")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())