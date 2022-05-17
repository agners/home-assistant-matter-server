import asyncio

from fastapi_websocket_rpc import RpcMethodsBase, WebSocketRpcClient

from matter_server import MyClusterObjects
from matter_server.MyObjects import *


class MatterClient(RpcMethodsBase):

    def __init__(self):
        super().__init__()
    
    async def some_event(self):
        print("some_event")
    
async def run_client(uri):
    client = WebSocketRpcClient(uri, MatterClient())
    await client.__connect__()
    response = await client.other.get_object()
    print(response)
    await asyncio.sleep(10)
    await client.close()

# run the client until it completes interaction with server
asyncio.run(
    run_client("ws://localhost:9000/ws")
)

