
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


if __name__ == '__main__':
    unittest.main()
