
import unittest
import device
import os


class TestMotherboard(unittest.TestCase):
    def test_bios_revision(self):
        handler = device.Device()
        print(handler.motherboard.bios_revision)

    def test_name(self):
        handler = device.Device()
        print(handler.motherboard.name)


if __name__ == '__main__':
    unittest.main()
