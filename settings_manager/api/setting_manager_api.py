# Internal import
from settings_manager.core.permission_group import PermissionGroup
from settings_manager.core.settings_type import SettingsType
from settings_manager.core.settings import Settings
from settings_manager.core.settings_user import SettingsUser

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
    def __init__(self, instance: str, username: str = None, script_name: str = None, password: str = None):

        self._instance = instance
        self._username = username
        self._script_name = script_name
        self._password = password

    """
    CRUD functions to directly read and update settings data
    """

    def read(self, settings_name: str, scope: SCOPE_TYPE = None) -> SettingsType:
        #TODO: To replace with real value
        return SettingsType()

    def update(self, settings: SETTINGS_TYPE, value: SettingsType, scope: SCOPE_TYPE = None) -> bool:
        return True

    def delete(self, settings: SETTINGS_TYPE, value: SettingsType, scope: SCOPE_TYPE = None) -> bool:
        return True

    def create(self, settings: SETTINGS_TYPE, value: SettingsType, scope: SCOPE_TYPE = None) -> bool:
        return True

    """
    CRUD functions to directly update settings database schema
    """

    def add_scope(self, scope_name: str, overridden_scopes: SCOPE_LIST_TYPE = None) -> bool:
        return True

    def delete_scope(self, scope_name: str) -> bool:
        return True

    def add_settings(self, settings_name: str, settings_type: SettingsType, scopes: SCOPE_LIST_TYPE = None,
                     permissions_groups: PERMISSION_GROUP_LIST_TYPE = None) -> Settings:
        return Settings()

    def update_settings(self, settings_name: str, settings_type: SettingsType, scopes: SCOPE_LIST_TYPE = None,
                        permissions_groups: PERMISSION_GROUP_LIST_TYPE = None) -> bool:
        return True

    def delete_settings(self, settings_name: SETTINGS_TYPE) -> bool:
        return True

    def add_permission_group(self, permission_group_name: str, users: USER_LIST_TYPE = None,
                             scripts: SCRIPT_LIST_TYPE = None) -> PermissionGroup:
        return PermissionGroup(permission_group_name, users, scripts)

    def update_permission_group(self, permission_group_name: str, users: USER_LIST_TYPE = None,
                                scripts: SCRIPT_LIST_TYPE = None) -> bool:
        return True

    def delete_permission_group(self, permission_group_name: str) -> bool:
        return True

    def add_user(self, user_name: str, permission_group: PERMISSION_GROUP_TYPE = None) -> SettingsUser:
        return SettingsUser(user_name)

    def delete_user(self, user_name: USER_TYPE) -> bool:
        return True

    def add_script(self, script_name: str, permission_group: PERMISSION_GROUP_TYPE = None):
        return True

    def delete_script(self, script_name: SCRIPT_TYPE) -> bool:
        return True
