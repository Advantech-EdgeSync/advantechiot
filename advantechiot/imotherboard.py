from abc import ABC, abstractmethod
from typing import List


class IMotherboard(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def bios_revision(self) -> str:
        pass

    @property
    @abstractmethod
    def voltage_sources(self) -> List[str]:
        pass

    @abstractmethod
    def get_voltage(self, voltage_source) -> float:
        pass

    @property
    @abstractmethod
    def temperature_sources(self) -> List[str]:
        pass

    @abstractmethod
    def get_temperature(self, temperature_source) -> float:
        pass

    @property
    @abstractmethod
    def fan_source(self) -> List[str]:
        pass

    @abstractmethod
    def get_fan_speed(self, fan_source) -> float:
        pass
