# pip install websockets
import asyncio
import websockets

async def echo(websocket, path):
    message = await websocket.recv()
    print(f"Received from client: {message}")
    # 여기서는 클라이언트로부터 받은 메시지를 그대로 다시 보냅니다.
    await websocket.send(message)

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
