from abc import ABC, abstractmethod


class SettingsDatabase(ABC):

    @abstractmethod
    def connect(self, identifier: str, password: str) -> bool:
        return True

    """
    @abstractmethod
    def read_settings(self, settings_name):
        value = None
        return value

    @abstractmethod
    def read(self, entity_type, entity_name, **filters):
        value = None
        return value

    @abstractmethod
    def create(self, entity_type, entity_name, entity_value, **extra_fields):
        return True

    @abstractmethod
    def update(self, entity_type, entity_name, entity_value, **filters):
        return True

    @abstractmethod
    def delete(self, entity_type, entity_name, **filters):
        return True
    
    """
