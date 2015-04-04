import sys
import threading

import serial

from time import sleep
from blessings import Terminal

SYNC = 0x80
PULSE = 0x40

OUTPUT = """
Heartrate:\t\t {}
Oxygen saturation:\t {}
Pulse waveform:\t\t {}

Hit Ctrl+C to exit.
"""

class PulseOximeterReader(object):
    """
    This class reads data from a Contec CMS50E pulse oximeter. The data
    is read by a separate thread.

    The data is output to the terminal. Use the `run` method to start.
    """

    def __init__(self,
                 port,
                 baudrate=19200,
                 timeout=2,
                 parity=serial.PARITY_ODD):

        self.waveform = 0
        self.heartrate = 0
        self.oxygen = 0

        self.reading = False
        self.terminal = Terminal()
        self.thread = None

        self.serial = serial.Serial(port,
                                    baudrate=baudrate,
                                    timeout=timeout,
                                    parity=parity)

    def run(self):
        self.reading = True

        self.sync_stream()

        self.thread = threading.Thread(target=self._run_thread)
        self.thread.start()

        try:
            while self.thread.is_alive():
                self.print_output()
                sleep(0.05)
        except KeyboardInterrupt:
            self.reading = False

    def sync_stream(self):
        """Find the sync bit and read five and five bytes from there."""
        while True:
            data = self.serial.read(5)

            for i, byte in enumerate(data):
                if byte & SYNC:
                    self.serial.read(i)  # throw away subsequent i bytes
                    return

    def _run_thread(self):
        while self.reading:
            data = self.serial.read(5)
            self.process_data(data)

    def process_data(self, data):
        """Process the data and store it on the reader."""
        data = self.serial.read(5)

        # In case we go out of sync, re-synchronise the stream.
        # This might happen if data upload is enabled on the device.
        if not data[0] & SYNC:
            self.sync_stream()

        self.waveform = data[1]
        self.heartrate = data[3]
        self.oxygen = data[4]

    def print_output(self):
        with self.terminal.fullscreen():
            print(
                OUTPUT.format(
                    self.heartrate, self.oxygen, self.waveform
                )
            )


if __name__ == '__main__':
    if not sys.argv[1]:
        print('Please provide the device identifier as an argument.')

    reader = PulseOximeterReader(sys.argv[1])
    reader.run()
