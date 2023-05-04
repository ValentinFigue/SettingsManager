from settings_manager.database.settings_database import SettingsDatabase

from settings_manager.core.settings_type import SettingsType


class MockDatabase(SettingsDatabase):

    def __init__(self):

        self._data = {}

    def connect(self, identifier: str, password: str) -> bool:
        return True

    def read_settings(self, settings_name: str, **filters) -> SettingsType:
        return self._data.get(settings_name)

    def create_settings(self, settings_name: str, entity_value: SettingsType, **extra_fields) -> bool:

        self._data[settings_name] = entity_value

        return True

    def update_settings(self, settings_name: str, entity_value: SettingsType, **filters) -> bool:

        self._data[settings_name] = entity_value

        return True

    def delete_settings(self, settings_name: str, **filters) -> bool:

        del self._data[settings_name]

        return True
