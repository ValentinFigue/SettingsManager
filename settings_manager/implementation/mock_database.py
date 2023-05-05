from settings_manager.database.settings_database import SettingsDatabase
from settings_manager.core.schema_settings_type import SchemaSettingsType
from settings_manager.constants.typing import SCHEMA_SCOPE_TYPE


class MockDatabase(SettingsDatabase):

    def __init__(self):

        self._data = {}
        self._scope_hierarchy={}

    def connect(self, identifier: str, password: str) -> bool:
        return True

    def read_settings(self, settings_name: str, **filters) -> SchemaSettingsType:
        return self._data.get(settings_name)

    def create_settings(self, settings_name: str, entity_value: SchemaSettingsType, **extra_fields) -> bool:

        self._data[settings_name] = entity_value

        return True

    def update_settings(self, settings_name: str, entity_value: SchemaSettingsType, **filters) -> bool:

        self._data[settings_name] = entity_value

        return True

    def delete_settings(self, settings_name: str, **filters) -> bool:

        del self._data[settings_name]

        return True

    def register_schema_scope(self, scope_name: str) -> bool:
        self._scope_hierarchy[scope_name] = None
        return True

    def unregister_schema_scope(self, scope_name: str) -> bool:

        del self._scope_hierarchy[scope_name]

        return True

    def check_schema_scope_existence(self, scope_name: str) -> bool:
        return scope_name in self._scope_hierarchy.keys()

    def parent_schema_scope(self, scope_name: str, overridden_scope: str) -> bool:

        if self._scope_hierarchy[overridden_scope] and self._scope_hierarchy[overridden_scope] != scope_name:
            return False
        else:
            self._scope_hierarchy[overridden_scope] = scope_name

        return True

    def unparent_schema_scope(self, scope_name: str, overridden_scope: str) -> bool:

        if self._scope_hierarchy[overridden_scope] and self._scope_hierarchy[overridden_scope] != scope_name:
            return False
        else:
            self._scope_hierarchy[overridden_scope] = None

        return True

    def get_schema_scope_overridden_by(self, scope_name: str) -> SCHEMA_SCOPE_TYPE:

        for scope in self._scope_hierarchy.keys():
            if scope_name == self._scope_hierarchy.get(scope):
                return scope
        return None

    def get_schema_scope_that_overrides(self, scope_name: str) -> SCHEMA_SCOPE_TYPE:

        return self._scope_hierarchy.get(scope_name)
