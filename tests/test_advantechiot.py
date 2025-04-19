
import unittest
import advantechiot
from enum import Enum


class GpioDirectionType(Enum):
    INPUT = 0
    OUTPUT = 1


class TestSDRAM(unittest.TestCase):
    def test_memory_count(self):
        device = advantechiot.Device()
        print(f"memory count: {device.memory.memory_count}")

    def test_get_memory_type(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} type:{handler.memory.get_memory_type(i)}")

    def test_get_module_type(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} module type:{handler.memory.get_module_type(i)}")

    def test_get_memory_size_in_GB(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} size in GB:{handler.memory.get_memory_size_in_GB(i)}")

    def test_get_memory_speed(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} speed:{handler.memory.get_memory_speed(i)} MT/s")

    def test_get_memory_rank(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} rank:{handler.memory.get_memory_rank(i)}")

    def test_get_memory_voltage(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} voltage:{handler.memory.get_memory_voltage(i)} v")

    def test_get_memory_bank(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} bank:{handler.memory.get_memory_bank(i)}")

    def test_get_memory_manufacturing_date_code(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} manufacturing date code week/year:{handler.memory.get_memory_manufacturing_date_code(i)}")

    def test_get_memory_temperature(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} temperature:{handler.memory.get_memory_temperature(i)} degrees Celsius")

    def test_get_memory_write_protection(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} write protection:{handler.memory.get_memory_write_protection(i)}")

    def test_get_memory_module_manufacture(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} module manufacture:{handler.memory.get_memory_module_manufacture(i)}")

    def test_get_memory_manufacture(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} manufacture:{handler.memory.get_memory_manufacture(i)}")

    def test_get_memory_part_number(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} part number:{handler.memory.get_memory_part_number(i)}")

    def test_get_memory_specific(self):
        handler = advantechiot.Device()
        for i in range(handler.memory.memory_count):
            print(
                f"memory{i} specific:{handler.memory.get_memory_specific(i)}")


class TestDiskInfo(unittest.TestCase):
    def test_total_disk_space(self):
        handler = advantechiot.Device()
        print(f"Total Disk Space: {handler.disk.total_disk_space} MB")

    def test_free_disk_space(self):
        handler = advantechiot.Device()
        print(f"Free Disk Space: {handler.disk.free_disk_space} MB")


class TestPlatformInformation(unittest.TestCase):
    def test_board_manufacturer(self):
        handler = advantechiot.Device()
        print(handler.motherboard.board_manufacturer)

    def test_name(self):
        handler = advantechiot.Device()
        print(handler.motherboard.name)

    def test_bios_revision(self):
        handler = advantechiot.Device()
        print(handler.motherboard.bios_revision)

    def test_library_version(self):
        handler = advantechiot.Device()
        print(handler.motherboard.library_version)


class TestHardwareMonitorVoltage(unittest.TestCase):
    def test_voltage_sources(self):
        device = advantechiot.Device()
        print()
        for voltage_sources in device.motherboard.voltage_sources:
            print(voltage_sources)

    def test_voltage(self):
        device = advantechiot.Device()
        print()
        for voltage_sources in device.motherboard.voltage_sources:
            print(voltage_sources, device.motherboard.get_voltage(voltage_sources))


class TestHardwareMonitorTemperature(unittest.TestCase):
    def test_temperature_sources(self):
        handler = advantechiot.Device()
        print()
        for source in handler.motherboard.temperature_sources:
            print(source)

    def test_get_temperature(self):
        handler = advantechiot.Device()
        print()
        for source in handler.motherboard.temperature_sources:
            print(
                f"{source}: {handler.motherboard.get_temperature(source)} degrees Celsius")


class TestHardwareMonitorFanSpeed(unittest.TestCase):
    def test_fan_sources(self):
        handler = advantechiot.Device()
        print()
        for source in handler.motherboard.fan_sources:
            print(source)


class TestListAndCount(unittest.TestCase):
    def test_memory_list(self):
        handler = advantechiot.Device()
        print()
        for source in handler.memory.memory_list:
            print(source)


class TestGpio(unittest.TestCase):
    def test_gpio_pins(self):
        device = advantechiot.Device()
        print()
        for gpio_name in device.gpio.pins:
            print(gpio_name)

    def test_get_gpio_direction(self):
        device = advantechiot.Device()
        print()
        for gpio_name in device.gpio.pins:
            print(
                f"{gpio_name}, direction:{device.gpio.get_direction(gpio_name)}")

    def test_set_gpio_direction(self):
        device = advantechiot.Device()
        original_dir = 0
        updated_dir = 0
        print()
        for gpio_name in device.gpio.pins:
            original_dir = device.gpio.get_direction(gpio_name)
            print(f"{gpio_name} original is {original_dir}")
            updated_dir = original_dir ^ 1
            device.gpio.set_direction(gpio_name, GpioDirectionType.INPUT)
            updated_dir = device.gpio.get_direction(gpio_name)
            print(f"{gpio_name} updated is {updated_dir}")
            device.gpio.set_direction(gpio_name, GpioDirectionType.OUTPUT)

    def test_get_gpio_level(self):
        device = advantechiot.Device()
        print()
        for gpio_name in device.gpio.pins:
            print(f"{gpio_name}, direction:{device.gpio.get_level(gpio_name)}")

    def test_set_gpio_level(self):
        pass


if __name__ == '__main__':
    unittest.main()
