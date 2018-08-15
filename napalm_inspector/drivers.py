from builtins import super
from napalm_inspector.exceptions import MissingData
from napalm.ios import IOSDriver
from napalm.nxos_ssh import NXOSSSHDriver
import re


class DummyDevice:

    def __init__(self, data):
        self.data = data

    def send_command(self, command):
        label = re.sub(r"[\[\]\*\^\+\s\|]", "_", command)
        if label not in self.data:
            raise MissingData(command)

        return self.data[label]


class OfflineIOSDriver(IOSDriver):

    def __init__(self, data):
        super().__init__("127.0.0.1", "", "")
        self.device = DummyDevice(data)


class OfflineNXOSSSHDriver(NXOSSSHDriver):

    def __init__(self, data):
        self.device = DummyDevice(data)


test_drivers = {"ios": OfflineIOSDriver, "nxos_ssh": OfflineNXOSSSHDriver}
