import asyncio
import websockets

TOKEN = "secure-token-123"

async def send_messages():
    uri = "ws://localhost:12345"
    try:
        async with websockets.connect(uri, subprotocols=[TOKEN]) as websocket:
            message = f"erhaan baraab"
            print(f"Sending: {message}")
            await websocket.send(message)
    except ConnectionRefusedError:
        print("Could not connect to Server 1")
    except websockets.InvalidHandshake:
        print("Handshake failed. Invalid token.")

if __name__ == "__main__":
    asyncio.run(send_messages())
