from logging import DEBUG, getLogger

import chip.FabricAdmin
import chip.native
from chip.ChipStack import *
from fastapi_websocket_rpc import RpcMethodsBase
from pydantic import BaseModel

logger = getLogger(__name__)
logger.setLevel(DEBUG)


class OnOff(BaseModel):
     onOff: bool = True

class MatterServer(RpcMethodsBase):
    """Main MatterServer implementation."""
    def __init__(self):
        self._channels = []
        logger.info("Starting CHIP stack")
        chip.native.GetLibraryHandle()
        self._stack = ChipStack(persistentStoragePath="/tmp/repl-storage.json")

        self._fabricAdmin = chip.FabricAdmin.FabricAdmin()

        self._devController = self._fabricAdmin.NewController()
        logger.info("CHIP stack initialized")

    async def get_object(self):
        return OnOff(onOff=True)

    async def on_connect(self, channel):
        logger.info(f"Client disconnected {channel}")
        self._channels.append(channel)
    async def on_disconnect(self, channel):
        logger.info(f"Client disconnected {channel}")
        self._channels.remove(channel)

    def shutdown(self):
        logger.info("Shutdown CHIP stack")
        self._devController.Shutdown()
        self._stack.Shutdown()
