import asyncio
import websockets.exceptions
from starlette.applications import Starlette
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket


async def ws_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        while True:
            await websocket.send_text('Hello, world!')
            await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosed:
        return



app = Starlette(debug=True, routes=[
    WebSocketRoute('/ws', ws_endpoint),
])
