from typing import Iterable

# Internal import
from settings_manager.core.permission_group import PermissionGroup
from settings_manager.core.schema_settings_type import SchemaSettingsType
from settings_manager.core.settings import Settings
from settings_manager.core.settings_user import SettingsUser
from settings_manager.core.schema_scope import SchemaScope
from settings_manager.core.schema_settings import SchemaSettings

from settings_manager.database.settings_database_api import SettingsDatabaseAPI
from settings_manager.database.settings_database_api import SettingsDatabase

from settings_manager.constants.typing import SCOPE_TYPE
from settings_manager.constants.typing import SCHEMA_SCOPE_TYPE
from settings_manager.constants.typing import SCOPE_LIST_TYPE
from settings_manager.constants.typing import SETTINGS_TYPE
from settings_manager.constants.typing import PERMISSION_GROUP_LIST_TYPE
from settings_manager.constants.typing import USER_LIST_TYPE
from settings_manager.constants.typing import SCRIPT_LIST_TYPE
from settings_manager.constants.typing import USER_TYPE
from settings_manager.constants.typing import SCRIPT_TYPE
from settings_manager.constants.typing import PERMISSION_GROUP_TYPE
from settings_manager.constants.typing import SCHEMA_SCOPE_LIST_TYPE


class SettingsManagerAPI:
    def __init__(self, settings_database: SettingsDatabase, username: str = None, script_name: str = None,
                 user_password: str = None, script_key: str = None):

        self._username = username
        self._script_name = script_name

        if not username and not script_name:
            raise ValueError('User name or script name must be set')
        if username and user_password:
            self._database_api = SettingsDatabaseAPI(settings_database, username, user_password)
        elif script_name and script_key:
            self._database_api = SettingsDatabaseAPI(settings_database, username, script_key)
        else:
            raise ValueError('Password for either scripts or users must be set to access the database')
    """
    CRUD functions to directly read and update settings data
    """

    def read_settings(self, settings_name: SETTINGS_TYPE, scope: SCOPE_TYPE = None) -> SchemaSettingsType:

        # Read value from settings database via database api
        value = self._database_api.read(Settings, str(settings_name), scope=scope)

        return value

    def update_settings(self, settings: SETTINGS_TYPE, value: SchemaSettingsType, scope: SCOPE_TYPE = None) -> bool:

        # Update value from settings database via database api
        status = self._database_api.update(Settings, str(settings), value, scope=scope)

        return status

    def delete_settings(self, settings: SETTINGS_TYPE, scope: SCOPE_TYPE = None) -> bool:

        status = self._database_api.delete(Settings, str(settings), scope=scope)

        return status

    def create_settings(self, settings: SETTINGS_TYPE, value: SchemaSettingsType, scope: SCOPE_TYPE = None) -> bool:

        status = self._database_api.create(Settings, str(settings), entity_value=value, scope=scope)

        return status

    """
    CRUD functions to directly update settings database schema
    """

    def add_scope_to_database(self, scope_name: str, override: SCHEMA_SCOPE_TYPE = None,
                              overridden_by: SCHEMA_SCOPE_TYPE = None, replace_override: bool = False) -> bool:

        # Convert to string scope inputs
        scope_name = self.convert_scope_to_string(scope_name)
        override = self.convert_scope_to_string(override)
        overridden_by = self.convert_scope_to_string(overridden_by)

        status = self._database_api.create(SchemaScope, scope_name, override=override,
                                           overridden_by=overridden_by, replace_override=replace_override)

        return status

    def delete_scope_from_database(self, scope_name: SCHEMA_SCOPE_TYPE) -> bool:

        # Convert to string scope inputs
        scope_name = self.convert_scope_to_string(scope_name)
        status = self._database_api.delete(SchemaScope, str(scope_name))

        return status

    def add_schema_settings_type_to_database(self, schema_settings_name: str, schema_settings_type: type) -> bool:

        status = self._database_api.create(SchemaSettingsType,
                                           schema_settings_name,
                                           settings_type=schema_settings_type)

        return status

    def delete_schema_settings_type_from_database(self, schema_settings_name: str) -> bool:

        status = self._database_api.delete(SchemaSettingsType,
                                           schema_settings_name)

        return status

    def add_settings_to_database(self, settings_name: str,
                                 schema_settings_type: SchemaSettingsType,
                                 scopes: SCHEMA_SCOPE_LIST_TYPE = None,
                                 permissions_groups: PERMISSION_GROUP_LIST_TYPE = None) -> bool:

        # Convert to string scope inputs
        scopes = self.convert_scopes_to_string_list(scopes)

        status = self._database_api.create(SchemaSettings,
                                           settings_name,
                                           schema_settings_type=SchemaSettingsType,
                                           schema_scopes=scopes,
                                           permissions_groups=permissions_groups)

        return status

    def update_settings_from_database(self, settings_name: str, settings_type: SchemaSettingsType, scopes: SCOPE_LIST_TYPE = None,
                                      permissions_groups: PERMISSION_GROUP_LIST_TYPE = None) -> bool:
        return True

    def delete_settings_from_database(self, settings_name: SETTINGS_TYPE) -> bool:
        return True

    def add_permission_group_to_database(self, permission_group_name: str, users: USER_LIST_TYPE = None,
                             scripts: SCRIPT_LIST_TYPE = None) -> PermissionGroup:
        return PermissionGroup(permission_group_name, users, scripts)

    def update_permission_group_from_database(self, permission_group_name: str, users: USER_LIST_TYPE = None,
                                scripts: SCRIPT_LIST_TYPE = None) -> bool:
        return True

    def delete_permission_group_from_database(self, permission_group_name: str) -> bool:
        return True

    def add_user_to_database(self, user_name: str, permission_group: PERMISSION_GROUP_TYPE = None) -> SettingsUser:
        return SettingsUser(user_name)

    def delete_user_from_database(self, user_name: USER_TYPE) -> bool:
        return True

    def add_script_to_database(self, script_name: str, permission_group: PERMISSION_GROUP_TYPE = None):
        return True

    def delete_script_from_database(self, script_name: SCRIPT_TYPE) -> bool:
        return True

    @staticmethod
    def convert_scope_to_string(scope: SCHEMA_SCOPE_TYPE) -> str:
        if isinstance(scope, SchemaScope):
            scope = str(scope)
        return scope

    @staticmethod
    def convert_scopes_to_string_list(scopes: SCHEMA_SCOPE_LIST_TYPE) -> Iterable[str]:
        converted_scopes = []
        if scopes:
            if isinstance(scopes, (SchemaScope, str)):
                converted_scopes.append(str(SchemaScope))
            else:
                for scope in scopes:
                    converted_scopes.append(str(scope))

        return converted_scopes
