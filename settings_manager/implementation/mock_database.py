from typing import Any

from settings_manager.database.settings_database import SettingsDatabase
from settings_manager.constants.typing import SCHEMA_SCOPE_TYPE
from settings_manager.constants.typing import STRING_LIST_TYPE
from settings_manager.constants.typing import SCHEMA_SCOPE_LIST_TYPE

class MockDatabase(SettingsDatabase):

    def __init__(self):

        self._data = {}
        self._scope_hierarchy = {}
        self._settings_type = {}
        self._settings_schema = {}
        self._scopes = {}

    def connect(self, identifier: str, password: str) -> bool:
        return True

    def get_settings(self, settings_name: str, scope: str, schema_scope: str) -> Any:

        return self._data.get(schema_scope, {}).get(scope, {}).get(settings_name)

    def set_settings(self, settings_name: str, entity_value: Any, scope: str, schema_scope: str) -> bool:

        self._data[schema_scope][scope][settings_name] = entity_value

        return True

    def register_settings(self, settings_name: str, entity_value: Any, scope: str, schema_scope: str) -> bool:

        self._data[schema_scope][scope][settings_name] = entity_value

        return True

    def unregister_settings(self, settings_name: str, scope: str, schema_scope: str) -> bool:

        del self._data[schema_scope][scope][settings_name]

        return True

    def check_settings_existence(self, settings_name: str, scope_name: str, schema_scope: str) -> bool:

        return settings_name in self._data[schema_scope][scope_name]

    def register_schema_scope(self, scope_name: str) -> bool:
        self._scope_hierarchy[scope_name] = None
        self._scopes[scope_name] = []
        self._data[scope_name] = {}

        return True

    def unregister_schema_scope(self, scope_name: str) -> bool:

        del self._scope_hierarchy[scope_name]
        del self._scopes[scope_name]
        del self._data[scope_name]

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

    def register_schema_settings_type(self, settings_type_name: str, settings_type: type) -> bool:

        self._settings_type[settings_type_name] = settings_type

        return True

    def unregister_schema_settings_type(self, settings_type_name: str) -> bool:

        del self._settings_type[settings_type_name]

        return True

    def check_schema_settings_type_existence(self, settings_type_name: str) -> bool:

        return settings_type_name in self._settings_type

    def check_schema_settings_existence(self, settings_name: str) -> bool:

        return settings_name in self._settings_schema

    def register_schema_settings(self, settings_name: str, schema_settings_type: str,
                                 schema_scopes:  STRING_LIST_TYPE,
                                 permissions_groups:  STRING_LIST_TYPE) -> bool:

        self._settings_schema[settings_name] = {}
        self._settings_schema['type'] = schema_settings_type
        self._settings_schema['scopes'] = schema_scopes
        self._settings_schema['permissions'] = permissions_groups

        return True

    def unregister_schema_settings(self, settings_name: str) -> bool:

        del self._settings_schema[settings_name]

        return True

    def set_schema_settings(self, settings_name: str, schema_settings_type: str,
                            schema_scopes:  STRING_LIST_TYPE,
                            permissions_groups:  STRING_LIST_TYPE) -> bool:

        self._settings_schema[settings_name] = {}
        self._settings_schema[settings_name]['type'] = schema_settings_type
        self._settings_schema[settings_name]['scopes'] = schema_scopes
        self._settings_schema[settings_name]['permissions'] = permissions_groups

        return True

    def check_scope_existence(self, scope_name: str, schema_scope_name: str) -> bool:

        return scope_name in self._scopes[schema_scope_name]

    def register_scope(self, scope_name: str, schema_scope_name: str) -> bool:

        self._scopes[schema_scope_name].append(scope_name)
        self._data[schema_scope_name][scope_name] = {}

        return True

    def unregister_scope(self, scope_name: str, schema_scope_name: str) -> bool:

        self._scopes[schema_scope_name].remove(scope_name)
        del self._data[schema_scope_name][scope_name]

        return True

    def get_settings_type(self, settings_name: str) -> type:

        return self._settings_type[self._settings_schema[settings_name]['type']]

    def get_settings_scope(self, settings_name: str) -> SCHEMA_SCOPE_LIST_TYPE:
        return self._settings_schema[settings_name]['scopes']