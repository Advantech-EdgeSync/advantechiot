
import os
import importlib.util
from .susiiot import SusiIot


class Device:
    def __init__(self):
        self.motherboard = None
        self.gpio = None
        self.watch_dog = None
        self.memory = None
        self.disk_information = None

        # if os.path.exists("/etc/board"):
        #     device_number = None
        #     device_number = os.system("cat /etc/board")
        #     print(f"device number: {device_number}")
        # else:
        #     print("/etc/board doesn't exist.")

        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # pyc_path=os.path.join(current_dir, "susiiot.pyc")
        # print(f"pyc_path: {pyc_path}")
        # spec = importlib.util.spec_from_file_location("susiiot", pyc_path)
        # SUSIIOT = importlib.util.module_from_spec(spec)
        # spec.loader.exec_module(SUSIIOT)
        # susiiot_object = SUSIIOT.SusiIot()
        
        susiiot_object = SusiIot()

        self.motherboard = susiiot_object
        self.gpio = susiiot_object
        self.watch_dog = susiiot_object
        self.memory = susiiot_object
        self.disk_information = susiiot_object

    def is_support_susiiot(device_number):
        susiiot_support_list = [
            "EPC-T4286",
        ]
        if device_number in susiiot_support_list:
            return True
        return False

    def is_support_platform_sdk(device_number):
        platform_sdk_support_list = [
            "",
        ]
        if device_number in platform_sdk_support_list:
            return True
        return False
