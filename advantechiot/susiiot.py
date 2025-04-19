import ctypes
import json
import sys
import os
import platform
from .imotherboard import IMotherboard
from .igpio import IGpio, GpioDirectionType, GpioLevelType
from .imemory import IMemory
from .idisk import IDisk
from typing import List


class SusiIot(IMotherboard, IGpio, IMemory, IDisk):
    def __init__(self):
        self.susi_iot_library = None
        self.json_library = None
        self.susi_information = None
        self.device_id_list=[]
        self.gpio_list = None
        # self.memory_list = []
        self.voltage_source_list = None
        self.temperature_source_list = None
        # self.susi_id_name_table = {}
        # self.susi_name_id_table = {}

        self.check_root_authorization()
        self.import_library()
        self.initialize_library()
        self.susi_iot_library.SusiIoTInitialize()
        self.get_susi_information_string()
        self.get_device_id_list()
        # self.get_gpio_list()
        # self.get_sdram_list()
        # self.get_name_id_list()

    def __del__(self):
        pass
        # self.susi_iot_library.SusiIoTUninitialize()

    def check_root_authorization(self):
        if os.geteuid() != 0:
            sys.exit("Error: Please run this program as root (use sudo).")
        else:
            return True


    def extract_ids(self,obj, result=None):
        if result is None:
            result = []

        if isinstance(obj, dict):
            # 如果有 id，就加入 list
            if "id" in obj:
                result.append(obj["id"])
            for value in obj.values():
                self.extract_ids(value, result)

        elif isinstance(obj, list):
            for item in obj:
                self.extract_ids(item, result)

        return result
    
    def get_device_id_list(self):
        self.device_id_list = self.extract_ids(self.susi_information)
    
    # def read_mock_data(self, data):
    #     self.susi_information = data

    # def get_name_id_list(self):
    #     data_sort = "Platform Information"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for item in self.susi_information[data_sort]["e"]:
    #             self.susi_id_name_table.update({item["n"]: item["id"]})
    #     except:
    #         pass

    #     data_sort = "Hardware Monitor"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for item in self.susi_information[data_sort]:
    #             if "id" in item or "bn" in item:
    #                 pass
    #             else:
    #                 sources = self.susi_information[data_sort][item]['e']
    #                 for source in sources:
    #                     self.susi_id_name_table.update(
    #                         {item+" "+source["n"]: source["id"]})
    #     except:
    #         pass

    #     data_sort = "Voltage"
    #     try:
    #         for key in self.susi_id_name_table.keys():
    #             if data_sort in key:
    #                 self.voltage_source_list.append(key)
    #     except:
    #         pass

    #     data_sort = "Temperature"
    #     try:
    #         for key in self.susi_id_name_table.keys():
    #             if data_sort in key:
    #                 self.temperature_source_list.append(key)
    #     except:
    #         pass

    #     data_sort = "GPIO"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for data_index in self.susi_information[data_sort].keys():
    #             if "GPIO" in data_index:
    #                 self.susi_id_name_table.update(
    #                     {data_index: self.susi_information[data_sort][data_index]["id"]})
    #                 for informations in self.susi_information[data_sort][data_index]["e"]:
    #                     self.susi_id_name_table.update(
    #                         {data_index+" "+informations["n"]: informations["id"]})
    #     except:
    #         pass

    #     data_sort = "SDRAM"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for data_index in self.susi_information[data_sort].keys():
    #             if "SDRAM" in data_index:
    #                 self.susi_id_name_table.update(
    #                     {data_index: self.susi_information[data_sort][data_index]["id"]})
    #                 for informations in self.susi_information[data_sort][data_index]["e"]:
    #                     self.susi_id_name_table.update(
    #                         {data_index+" "+informations["n"]: informations["id"]})
    #     except:
    #         pass

    #     data_sort = "DiskInfo"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for data_index in self.susi_information[data_sort]["e"]:
    #             self.susi_id_name_table.update(
    #                 {data_index["n"]: data_index["id"]})
    #     except:
    #         pass

    #     data_sort = "SUSIIoT Information"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for data_index in self.susi_information[data_sort]["e"]:
    #             self.susi_id_name_table.update(
    #                 {data_index["n"]: data_index["id"]})
    #     except:
    #         pass

    #     data_sort = "M2Talk"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for data_index in self.susi_information[data_sort].keys():
    #             if "Device" in data_index:
    #                 sources = self.susi_information[data_sort][data_index]['e']
    #                 for source in sources:
    #                     self.susi_id_name_table.update(
    #                         {data_sort+" "+source['n']: source['id']})
    #     except:
    #         pass

    #     data_sort = "Backlight"
    #     try:
    #         id_value = self.susi_information[data_sort]["id"]
    #         self.susi_id_name_table.update({data_sort: id_value})
    #         for data_index in self.susi_information[data_sort].keys():
    #             if "Backlight" in data_index:
    #                 sources = self.susi_information[data_sort][data_index]['e']
    #                 for source in sources:
    #                     self.susi_id_name_table.update(
    #                         {data_sort+" "+source['n']: source['id']})
    #     except:
    #         pass

    def import_library(self):
        architecture = platform.machine()
        os_name = platform.system()
        susi_iot_library_path = ""
        json_library_path = ""

        if os_name == "Linux" and 'x86' in architecture.lower():
            susi_iot_library_path = "/usr/lib/libSusiIoT.so"
            json_library_path = "/usr/lib/x86_64-linux-gnu/libjansson.so.4"

        elif os_name == "Linux" and 'aarch64' in architecture.lower():
            susi_iot_library_path = "/lib/libSusiIoT.so"
            json_library_path = "/lib/aarch64-linux-gnu/libjansson.so.4"

        elif os_name == "Windows" and 'x86' in architecture.lower():
            pass

        elif os_name == "Windows" and 'aarch64' in architecture.lower():
            pass

        else:
            print(
                f"disable to import library, architechture:{architecture.lower()}, os:{os_name}")

        self.json_library = ctypes.CDLL(
            json_library_path, mode=ctypes.RTLD_GLOBAL)
        self.susi_iot_library = ctypes.CDLL(
            susi_iot_library_path, mode=ctypes.RTLD_GLOBAL)

    def initialize_library(self):
        # SusiIoTStatus_t = ctypes.c_int
        # SusiIoTId_t = ctypes.c_int

        self.susi_iot_library.SusiIoTInitialize.restype = ctypes.c_int

        self.susi_iot_library.SusiIoTSetValue.argtypes = [
            ctypes.c_uint32, ctypes.POINTER(JsonT)]
        self.susi_iot_library.SusiIoTSetValue.restype = ctypes.c_uint32

        self.susi_iot_library.SusiIoTGetLoggerPath.restype = ctypes.c_char_p

        self.susi_iot_library.SusiIoTGetPFDataString.restype = ctypes.c_char_p
        self.susi_iot_library.SusiIoTGetPFDataString.argtypes = [
            ctypes.c_uint32]

        self.susi_iot_library.SusiIoTGetPFDataStringByUri.restype = ctypes.c_char_p
        self.susi_iot_library.SusiIoTGetPFDataStringByUri.argtypes = [
            ctypes.c_char_p]

        self.json_library.json_dumps.restype = ctypes.c_char_p
        self.json_library.json_integer.restype = ctypes.POINTER(JsonT)

        self.json_library.json_real.restype = ctypes.POINTER(JsonT)
        self.json_library.json_string.restype = ctypes.POINTER(JsonT)
        prototype = ctypes.CFUNCTYPE(
            ctypes.c_char_p
        )
        self.SusiIoTGetPFCapabilityString = prototype(
            ("SusiIoTGetPFCapabilityString", self.susi_iot_library))

        self.susi_iot_library.SusiIoTUninitialize.restype = ctypes.c_int

    # def get_gpio_list(self):
    #     try:
    #         for key in self.susi_information["GPIO"].keys():
    #             if "GPIO" in key:
    #                 self.gpio_list.append(key)
    #     except:
    #         pass

    # def get_sdram_list(self):
    #     try:
    #         for key in self.susi_information["SDRAM"].keys():
    #             if "SDRAM" in key:
    #                 self.memory_list.append(key)
    #     except:
    #         pass

    def get_json_indent(self, n):
        json_max_indent = 0x1F
        return n & json_max_indent

    def get_json_real_precision(self, n):
        return ((n & 0x1F) << 11)

    def turn_byte_to_json(self, json_bytes):
        json_str = json_bytes.decode('utf-8')
        data = json.loads(json_str)
        return data

    def get_data_by_id(self, device_id):
        result = self.susi_iot_library.SusiIoTGetPFDataString(device_id)
        return self.turn_byte_to_json(result)

    def set_value(self, device_id, value):
        result_ptr = self.json_library.json_integer(value)
        result = result_ptr.contents
        return self.susi_iot_library.SusiIoTSetValue(device_id, result)

    def get_susi_information_string(self):
        capability_string = self.SusiIoTGetPFCapabilityString()
        capability_string = capability_string.decode('utf-8')
        try:
            self.susi_information = json.loads(capability_string)
        except json.JSONDecodeError as e:
            print("Failed to parse JSON.:", e)
        return self.susi_information

    def get_susi_information(self):
        json_max_indent = 0x1F
        jsonObject = self.json_library.json_object()
        if self.susi_iot_library.SusiIoTGetPFCapability(jsonObject) != 0:
            self.susi_information = "SusiIoTGetPFCapability failed."
            exit(1)
        else:
            self.susi_json_t = self.json_library.json_dumps(jsonObject, self.get_json_indent(
                4) | json_max_indent | self.get_json_real_precision(10))
            self.susi_information = self.turn_byte_to_json(self.susi_json_t)

        return self.susi_information

    @property
    def susi_iot_information(self):
        return self.susi_information

    @property
    def boot_up_times(self):
        id_number=16843010
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def running_time_in_hours(self):
        id_number=16843011
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def name(self):
        id_number=16843778
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def bios_revision(self):
        id_number=16843781
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def firmware_name(self):
        id_number=16843784
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def library_version(self):
        id_number=16843266
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def driver_version(self):
        id_number=16843265
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def firmware_version(self):
        id_number=16843267
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def voltage_vcore(self):
        id_number=16908801
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def voltage_3p3v(self):
        id_number=16908804
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def voltage_5v(self):
        id_number=16908805
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def voltage_12v(self):
        id_number=16908806
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def voltage_5v_standby(self):
        id_number=16908807
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def voltage_cmos_battery(self):
        id_number=16908809
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def dc_power(self):
        id_number=16908814
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]
    
    @property
    def voltage_3v(self):
        id_number=16908817
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def cpu_temperature(self):
        id_number=16908545
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def system_temperature_in_celsius(self):
        id_number=16908547
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    def get_gpio_direction(self, gpio_number=0):
        id_number=16908547
        result = self.get_data_by_id(id_number+gpio_number)
        if not result:
            return None
        return result["v"]

    def set_gpio_direction(self, gpio_number=0, direction=0):
        # todo
        try:
            gpio_string = self.gpio_list[gpio_number]
            id_number = self.susi_information["GPIO"][gpio_string]["e"][0]["id"]
            result = self.set_value(id_number, direction)
            if result != 0:
                return False
            return True
        except:
            return None

    def get_gpio_level(self, gpio_number=0):
        id_number=17040129
        result = self.get_data_by_id(id_number+gpio_number)
        if not result:
            return None
        return result["v"]

    def is_gpio_output(self, gpio_number=0):
        # todo
        try:
            gpio_string = self.gpio_list[gpio_number]
            id_number = self.susi_information["GPIO"][gpio_string]["e"][0]["id"]
            if self.get_data_by_id(id_number)['bv'] == 0:
                return True
        except:
            return False

    def is_gpio_output_with_gpio_name(self, gpio_name=0):
        # todo
        try:
            id_number = self.susi_information["GPIO"][gpio_name]["e"][0]["id"]
            if self.get_data_by_id(id_number)['bv'] == 0:
                return True
        except:
            return False

    def set_gpio_level(self, gpio_number=0, level=0):
        # todo
        gpio_direction_is_output = self.is_gpio_output(gpio_number)
        if not gpio_direction_is_output:
            return False
        gpio_string = self.gpio_list[gpio_number]
        id_number = self.susi_information["GPIO"][gpio_string]["e"][1]["id"]
        result = self.set_value(id_number, level)
        if result != 0:
            return False
        return True

    # @property
    # def memory_count(self):
    #     initial=337117185
    #     count=0
    #     for i in range(64):
    #         if initial+i in self.device_id_list:
    #             count+=1
    #         else:
    #             return count

    def get_memory_type(self, memory_number=0):
        id_number=337117441
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_module_type(self, memory_number=0):
        id_number=337117697
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_size_in_GB(self, memory_number=0):
        id_number=337117953
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_speed(self, memory_number=0):
        id_number=337118209
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_rank(self, memory_number=0):
        id_number=337118465
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_voltage(self, memory_number=0):
        id_number=337118721
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_bank(self, memory_number=0):
        id_number=337118977
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_manufacturing_date_code(self, memory_number=0):
        id_number=337119233
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_temperature(self, memory_number=0):
        id_number=337119489
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_write_protection(self, memory_number=0):
        id_number=337119745
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_module_manufacture(self, memory_number=0):
        id_number=337120001
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_manufacture(self, memory_number=0):
        id_number=337120257
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_part_number(self, memory_number=0):
        id_number=337121537
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    def get_memory_specific(self, memory_number=0):
        id_number=337125633
        result = self.get_data_by_id(id_number+memory_number)
        if not result:
            return None
        return result["v"]

    @property
    def total_disk_space(self):
        # todo, there are 2 item with the same id 353697792
        try:
            id_number = 353697792
            result = self.get_data_by_id(id_number)
            result = result['e'][0]
            if not result:
                print(f"{id_number} result is {result}")
            return result["v"]
        except:
            return None

    @property
    def free_disk_space(self):
        id_number=353697793
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def cpu_fan_speed(self):
        id_number=16909057
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def system_fan_speed(self):
        id_number=16909058
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["v"]

    @property
    def susiiot_version(self):
        id_number=257
        result = self.get_data_by_id(id_number)
        if not result:
            return None
        return result["sv"]

    @property
    def voltage_sources(self) -> List[str]:
        if self.voltage_source_list!=None:
            return self.voltage_source_list
        self.voltage_source_list=[]
        initial=16908801
        for i in range(20):
            if initial+i in self.device_id_list:
                name=self.get_data_by_id(initial+i)['n']
                self.voltage_source_list.append(name)
            else:
                return self.voltage_source_list 

    @property
    def temperature_sources(self) -> List[str]:
        if self.temperature_source_list!=None:
            return self.temperature_source_list
        self.temperature_source_list=[]
        # system temperature
        initial=16908545
        for i in range(20):
            if initial+i in self.device_id_list:
                name=self.get_data_by_id(initial+i)['n']
                self.temperature_source_list.append(name)

        # memory temperature
        initial=337119489
        for i in range(64):
            if initial+i in self.device_id_list:
                name=self.get_data_by_id(initial+i)['n']
                self.temperature_source_list.append(name)
        
        return self.temperature_source_list

    def get_voltage(self, voltage_source) -> float:
        try:
            id_number = self.susi_id_name_table[voltage_source]
            result = self.get_data_by_id(id_number)
            return float(result["v"])
        except:
            pass

    def get_temperature(self, temperature_source) -> float:
        try:
            id_number = self.susi_id_name_table[temperature_source]
            result = self.get_data_by_id(id_number)
            return float(result["v"])
        except:
            pass

    @property
    def fan_source(self) -> List[str]:
        pass

    def get_fan_speed(self, fan_source) -> int:
        pass

    @property
    def pins(self) -> List[str]:
        if self.gpio_list!=None:
            return self.gpio_list
        self.gpio_list=[]
        initial=17039617
        for i in range(64):
            if initial+i in self.device_id_list:
                name=self.get_data_by_id(initial+i)['bn']
                self.gpio_list.append(name)
            else:
                return self.gpio_list 

    @property
    def gpio_count(self):
        initial=17039617
        count=0
        for i in range(64):
            if initial+i in self.device_id_list:
                count+=1
            else:
                return count

    def get_direction(self, pin: str) -> None:
        try:
            id_number = self.susi_information["GPIO"][pin]["e"][0]["id"]
            return self.get_data_by_id(id_number)['bv']
        except:
            return None

    def set_direction(self, pin: str, direction: GpioDirectionType) -> None:
        try:
            id_number = self.susi_information["GPIO"][pin]["e"][0]["id"]
            result = self.set_value(id_number, direction)
            if result != 0:
                return False
            return True
        except:
            return None

    def get_level(self, pin: str) -> None:
        try:
            id_number = self.susi_information["GPIO"][pin]["e"][1]["id"]
            return self.get_data_by_id(id_number)['bv']
        except:
            return None

    def set_level(self, pin: str, level: GpioLevelType) -> None:
        gpio_direction_is_output = self.is_gpio_output_with_gpio_name(pin)
        if not gpio_direction_is_output:
            return False
            id_number = self.susi_information["GPIO"][pin]["e"][1]["id"]
            result = self.set_value(id_number, level)
            if result != 0:
                return False
        return True


class JsonType:
    JSON_OBJECT = 0
    JSON_ARRAY = 1
    JSON_STRING = 2
    JSON_INTEGER = 3
    JSON_REAL = 4
    JSON_TRUE = 5
    JSON_FALSE = 6
    JSON_NULL = 7


class JsonT(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_int),
        ("refcount", ctypes.c_size_t)
    ]

