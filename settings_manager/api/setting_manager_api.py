# Internal import
from settings_manager.core.permission_group import PermissionGroup
from settings_manager.core.settings_type import SettingsType
from settings_manager.core.settings import Settings
from settings_manager.core.settings_user import SettingsUser
from settings_manager.core.scope import Scope

from settings_manager.database.settings_database_api import SettingsDatabaseAPI
from settings_manager.database.settings_database_api import SettingsDatabase

from settings_manager.constants.typing import SCOPE_TYPE
from settings_manager.constants.typing import SCOPE_LIST_TYPE
from settings_manager.constants.typing import SETTINGS_TYPE
from settings_manager.constants.typing import PERMISSION_GROUP_LIST_TYPE
from settings_manager.constants.typing import USER_LIST_TYPE
from settings_manager.constants.typing import SCRIPT_LIST_TYPE
from settings_manager.constants.typing import USER_TYPE
from settings_manager.constants.typing import SCRIPT_TYPE
from settings_manager.constants.typing import PERMISSION_GROUP_TYPE


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

    def read_settings(self, settings_name: SETTINGS_TYPE, scope: SCOPE_TYPE = None) -> SettingsType:

        # Read value from settings database via database api
        value = self._database_api.read(Settings, str(settings_name), scope=scope)

        return value

    def update_settings(self, settings: SETTINGS_TYPE, value: SettingsType, scope: SCOPE_TYPE = None) -> bool:

        # Update value from settings database via database api
        status = self._database_api.update(Settings, str(settings), value, scope=scope)

        return status

    def delete_settings(self, settings: SETTINGS_TYPE, scope: SCOPE_TYPE = None) -> bool:

        status = self._database_api.delete(Settings, str(settings), scope=scope)

        return status

    def create_settings(self, settings: SETTINGS_TYPE, value: SettingsType, scope: SCOPE_TYPE = None) -> bool:

        status = self._database_api.create(Settings, str(settings), value, scope=scope)

        return status

    """
    CRUD functions to directly update settings database schema
    """

    def add_scope_to_database(self, scope_name: SCOPE_TYPE, overridden_scopes: SCOPE_LIST_TYPE = None) -> bool:

        # Convert scopes to override to string only
        if overridden_scopes and not isinstance(overridden_scopes, (str, Scope)):
            overridden_scopes = [str(overridden_scope) for overridden_scope in overridden_scopes]

        status = self._database_api.create(Scope, str(scope_name), overridden_scopes=overridden_scopes)

        return status

    def delete_scope_from_database(self, scope_name: SCOPE_TYPE) -> bool:

        status = self._database_api.delete(Scope, str(scope_name))

        return status

    def add_settings_to_database(self, settings_name: str, settings_type: SettingsType, scopes: SCOPE_LIST_TYPE = None,
                     permissions_groups: PERMISSION_GROUP_LIST_TYPE = None) -> Settings:
        return Settings()

    def update_settings_from_database(self, settings_name: str, settings_type: SettingsType, scopes: SCOPE_LIST_TYPE = None,
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
