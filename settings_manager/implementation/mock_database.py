from settings_manager.database.settings_database import SettingsDatabase
from settings_manager.core.settings_type import SettingsType
from settings_manager.constants.typing import SCOPE_LIST_TYPE


class MockDatabase(SettingsDatabase):

    def __init__(self):

        self._data = {}
        self._scope_hierarchy={}

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

    def create_scope(self, scope_name: str, overridden_scopes: SCOPE_LIST_TYPE) -> bool:

        self._scope_hierarchy[scope_name] = []
        if overridden_scopes:
            for scope in overridden_scopes:
                self._scope_hierarchy[scope].append(scope)

        return True
