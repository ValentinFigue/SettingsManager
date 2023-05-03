# External import
from typing import Union, Iterable

# Internal import
from settings_manager.core.scope import Scope
from settings_manager.core.permission_group import PermissionGroup
from settings_manager.core.settings_type import SettingsType
from settings_manager.core.settings import Settings
from settings_manager.core.settings_user import SettingsUser
from settings_manager.core.settings_script import SettingsScript

class SettingsManagerAPI:
    def __init__(self, instance: str, username: str = None, script_name: str = None, password: str = None):

        self._instance = instance
        self._username = username
        self._script_name = script_name
        self._password = password

    """
    CRUD functions to directly read and update settings data
    """

    def read(self, settings_name: str, scope: Union[str, Scope] = None) -> SettingsType:
        #TODO: To replace with real value
        return SettingsType()

    def update(self, settings: Union[str, Scope], value: SettingsType, scope: Union[str, Scope] = None) -> bool:
        return True

    def delete(self, settings: Union[str, Scope], value: SettingsType, scope: Union[str, Scope] = None) -> bool:
        return True

    def create(self, settings: Union[str, Scope], value: SettingsType, scope: Union[str, Scope] = None) -> bool:
        return True

    """
    CRUD functions to directly update settings database schema
    """

    def add_scope(self, scope_name: str,
                  overridden_scopes: Union[str, Scope, Iterable[Union[Scope, str], None]] = None) -> bool:
        return True

    def delete_scope(self, scope_name: str) -> bool:
        return True

    def add_settings(self, settings_name: str, settings_type: SettingsType,
                     scopes: Union[str, Scope, Iterable[Union[Scope, str], None]] = None,
                     permissions_groups: Union[str, PermissionGroup, Iterable[Union[PermissionGroup, str], None]] = None) -> Settings:
        return Settings()

    def update_settings(self, settings_name: str, settings_type: SettingsType,
                        scopes: Union[str, Scope, Iterable[Union[Scope, str], None]] = None,
                        permissions_groups: Union[str, PermissionGroup, Iterable[Union[PermissionGroup, str], None]] = None) -> bool:
        return True

    def delete_settings(self, settings_name: str) -> bool:
        return True

    def add_permission_group(self, permission_group_name: str,
                             users: Union[str, SettingsUser, Iterable[Union[SettingsUser, str], None]] = None,
                             scripts: Union[str, SettingsScript, Iterable[Union[SettingsScript, str], None]] = None) -> PermissionGroup:
        return PermissionGroup(permission_group_name, users, scripts)

    def update_permission_group(self, permission_group_name: str,
                                users: Union[str, SettingsUser, Iterable[Union[SettingsUser, str], None]] = None,
                                scripts: Union[str, SettingsScript, Iterable[Union[SettingsScript, str], None]] = None) -> bool:
        return True

    def delete_permission_group(self, permission_group_name: str,
                                users: Union[str, SettingsUser, Iterable[Union[SettingsUser, str], None]] = None,
                                scripts: Union[str, SettingsScript, Iterable[Union[SettingsScript, str], None]] = None) -> bool:
        return True

    def add_user(self, user_name: str, permission_group: Union[str, PermissionGroup] = None) -> SettingsUser:
        return SettingsUser(user_name)

    def delete_user(self, user_name: Union[str, SettingsUser]) -> bool:
        return True

    def add_script(self, script_name: str, permission_group: Union[str, PermissionGroup] = None):
        return True

    def delete_script(self, script_name: Union[str, SettingsUser]) -> bool:
        return True
