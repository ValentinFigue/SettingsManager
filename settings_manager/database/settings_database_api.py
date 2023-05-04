from settings_manager.database.settings_database import SettingsDatabase


class SettingsDatabaseAPI:

    def __init__(self, database: SettingsDatabase, identifier: str, password: str):

        self._database = database
        self._database.connect(identifier, password)

    def read(self, entity_type, entity_name, **filters):

        value = None
        return value

    def create(self, entity_type, entity_name, entity_value, **extra_fields):
        return True

    def update(self, entity_type, entity_name, entity_value, **filters):
        return True

    def delete(self, entity_type, entity_name, **filters):
        return True
