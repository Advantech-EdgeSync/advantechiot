from abc import ABC, abstractmethod

class IDisk(ABC):
    @property
    @abstractmethod
    def disk_total_disk_space(self) -> int:
        pass

    @property
    @abstractmethod
    def disk_free_disk_space(self) -> int:
        pass

    @property
    @abstractmethod
    def disk_media_recovery_total_disk_space(self) -> int:
        pass

    @property
    @abstractmethod
    def disk_media_recovery_free_disk_space(self) -> int:
        pass

    @property
    @abstractmethod
    def disk_home_total_disk_space(self) -> int:
        pass

    @property
    @abstractmethod
    def disk_home_free_disk_space(self) -> int:
        pass
