
import unittest
import advantechiot


class TestMotherboard(unittest.TestCase):
    def test_name(self):
        handler = advantechiot.device.Device()
        print(handler.motherboard.name)

    def test_bios_revision(self):
        handler = advantechiot.device.Device()
        print(handler.motherboard.bios_revision)

    def test_voltage_sources(self):
        handler = advantechiot.device.Device()
        print()
        for source in handler.motherboard.voltage_sources:
            print(source)

    def test_get_voltage(self):
        handler = advantechiot.device.Device()
        for source in handler.motherboard.voltage_sources:
            print(f"{source}: {handler.motherboard.get_voltage(source)}V")

    def test_temperature_sources(self):
        handler = advantechiot.device.Device()
        for source in handler.motherboard.temperature_sources:
            print(source)

    def test_get_temperature(self):
        handler = advantechiot.device.Device()
        print()
        for source in handler.motherboard.temperature_sources:
            print(f"{source}: {handler.motherboard.get_temperature(source)}")


class TestGpio(unittest.TestCase):
    def test_get_gpio_direction(self):
        handler = advantechiot.device.Device()
        print()
        print(handler.gpio.pins)
        for i in range(handler.gpio.gpio_counter):
            print(f"GPIO{i}, direction:{handler.gpio.get_gpio_direction(i)}")

    def test_get_gpio_level(self):
        handler = advantechiot.device.Device()
        print()
        print(handler.gpio.pins)
        for i in range(handler.gpio.gpio_counter):
            print(f"GPIO{i}, level:{handler.gpio.get_gpio_level(i)}")


class TestMemory(unittest.TestCase):
    def test_memory_count(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")

    def test_get_memory_type(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_type(i)}")

    def test_get_module_type(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_module_type(i)}")

    def test_get_memory_size_in_GB(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_size_in_GB(i)}")

    def test_get_memory_speed(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_speed(i)}")

    def test_get_memory_rank(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_rank(i)}")

    def test_get_memory_voltage(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_voltage(i)}")

    def test_get_memory_bank(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_bank(i)}")

    def test_get_memory_week_year(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory manufacture data:{handler.memory.get_memory_week_year(i)}")

    def test_get_memory_temperature(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} memory temperature:{handler.memory.get_memory_temperature(i)}")

    def test_get_memory_write_protection(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} write protection:{handler.memory.get_memory_write_protection(i)}")

    def test_get_memory_module_manufacture(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} module manufacture:{handler.memory.get_memory_module_manufacture(i)}")

    # @unittest.skip("todo")
    def test_get_memory_manufacture(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} manufacture:{handler.memory.get_memory_manufacture(i)}")

    def test_get_memory_part_number(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} part number:{handler.memory.get_memory_part_number(i)}")

    def test_get_memory_specific(self):
        handler = advantechiot.device.Device()
        print(f"memory count: {handler.memory.memory_count}")
        for i in range(handler.memory.memory_count):
            print(f"memory{i} specific:{handler.memory.get_memory_specific(i)}")


if __name__ == '__main__':
    unittest.main()
