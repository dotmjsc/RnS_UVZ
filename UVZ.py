import atexit
import logging
import time
from typing import Literal
import pyvisa

class UVZ:
    def __init__(self, address: str):
        self._rm = pyvisa.ResourceManager()
        self._inst = self._rm.open_resource(address)
        self._inst.clear()
        self._mode = "M0"
        self.mode = "M0"
        self._output = False
        self.output = False
        self._channel = 1
        self.channel = 1
        atexit.register(self._exit)

    def _exit(self):
        self._inst.clear()

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, mode: Literal["M0", "M1", "M2", "3p", "3p6p", "6p"]):
        if mode not in ["M0", "M1", "M2", "3p", "3p6p", "6p"]:
            logging.error("Mode must be one of those: M0, M1, M2, 3p, 3p6p, 6p")
            return
        if mode == '3p':
            mode = "M0"
        if mode == '3p6p':
            mode = "M1"
        if mode == '6p':
            mode = "M2"
        self._mode = mode
        self._inst.write(mode)

    @property
    def output(self) -> bool:
        return self._output

    @output.setter
    def output(self, state: bool):
        if state:
            self._inst.write("OE")
        else:
            self._inst.write("OD")
        self._output = state

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel: int):
        if self.mode == 'M0':
            if channel not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
                logging.error("Mode 0 only supports channel 1-16")
                return
        if self.mode == 'M1':
            if channel not in [1, 2, 3, 4, 5, 6, 7, 8, 21, 22, 23, 24]:
                logging.error("Mode 1 only supports channel 1-8 and 21-24")
                return
        if self.mode == 'M2':
            if channel not in [17, 18, 19, 20, 21, 22, 23, 24]:
                logging.error("Mode 0 only supports channel 17-24")
                return
        self._channel = channel
        self._inst.write("CH " + str(channel))


if __name__ == "__main__":
    uvz = UVZ('GPIB0::4::INSTR')
    uvz.mode = "M2"
    uvz.output = True
    uvz.channel = 18
    time.sleep(5)
