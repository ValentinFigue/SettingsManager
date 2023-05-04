from settings_manager.database.settings_database import SettingsDatabase


class MockDatabase(SettingsDatabase):

    def __init__(self):

        self._data = {}

    def connect(self, identifier: str, password: str) -> bool:
        return True

