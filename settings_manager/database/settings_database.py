from abc import ABC, abstractmethod

from settings_manager.core.settings_type import SettingsType


class SettingsDatabase(ABC):

    @abstractmethod
    def connect(self, identifier: str, password: str) -> bool:
        return True

    @abstractmethod
    def read_settings(self, settings_name: str, **filters) -> SettingsType:
        return

    @abstractmethod
    def create_settings(self, settings_name: str, entity_value: SettingsType, **extra_fields) -> bool:
        return

    @abstractmethod
    def update_settings(self, settings_name: str, entity_value: SettingsType, **filters) -> bool:
        return

    @abstractmethod
    def delete_settings(self, settings_name: str, **filters) -> bool:
        return

