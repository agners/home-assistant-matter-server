import asyncio
from dataclasses import dataclass
from logging import getLogger

import uvicorn
from fastapi import FastAPI
from fastapi_websocket_rpc import RpcMethodsBase, WebsocketRPCEndpoint

from .server import MatterServer

logger = getLogger(__name__)


async def on_connect(channel):
    # Wait a bit
    logger.info(f"Client connected: {channel}")
    await asyncio.sleep(1) 
    # now tell the client it can start sending us queries
    asyncio.create_task(channel.other.allow_queries())

def main() -> int:
    # Init the FAST-API app
    app =  FastAPI()
    # Create an endpoint and load it with the methods to expose
    matter_server = MatterServer()
    endpoint = WebsocketRPCEndpoint(matter_server, 
        on_connect=[matter_server.on_connect], 
        on_disconnect=[matter_server.on_disconnect])
    # add the endpoint to the app
    endpoint.register_route(app, "/ws")

    # Start the server itself
    uvicorn.run(app, host="0.0.0.0", port=9000)
    matter_server.shutdown()

