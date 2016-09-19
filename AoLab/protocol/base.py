# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 18-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc
from ..domain.message import AoLabThingMessage


class AoLabSerialProtocol:

    @abc.abstractmethod
    def write(self, type, device_id, node_id, command):
        pass

    @abc.abstractmethod
    def handle(self, message: str) -> AoLabThingMessage:
        pass
