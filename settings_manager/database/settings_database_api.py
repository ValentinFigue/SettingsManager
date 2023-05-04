from settings_manager.database.settings_database import SettingsDatabase

from settings_manager.core.settings import Settings


class SettingsDatabaseAPI:

    def __init__(self, database: SettingsDatabase, identifier: str, password: str):

        self._database = database
        self._database.connect(identifier, password)

    def read(self, entity_type, entity_name, **filters):

        if entity_type is Settings:
            value = self._database.read_settings(entity_name, **filters)

        return value

    def create(self, entity_type, entity_name, entity_value, **extra_fields):

        if entity_type is Settings:
            value = self._database.create_settings(entity_name, entity_value, **extra_fields)

        return value

    def update(self, entity_type, entity_name, entity_value, **filters):

        if entity_type is Settings:
            value = self._database.update_settings(entity_name, entity_value, **filters)

        return value

    def delete(self, entity_type, entity_name, **filters):

        if entity_type is Settings:
            value = self._database.delete_settings(entity_name, **filters)

        return value
