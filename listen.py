import asyncio
import websockets

TOKEN = "secure-token-123"

async def listen():
    uri = "ws://localhost:12345"
    try:
        async with websockets.connect(uri, subprotocols=[TOKEN], ping_interval=None) as websocket:
            print("Server 2 connected to Server 1.")
            async for message in websocket:
                print(f"Server 2 received: {message}")
    except ConnectionRefusedError:
        print("Could not connect to Server 1.")
    except websockets.InvalidHandshake:
        print("Handshake failed. Invalid token.")

if __name__ == "__main__":
    asyncio.run(listen())