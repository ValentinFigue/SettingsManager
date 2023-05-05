from typing import Union, Iterable

from settings_manager.core.scope import Scope
from settings_manager.core.schema_scope import SchemaScope
from settings_manager.core.permission_group import PermissionGroup
from settings_manager.core.settings import Settings
from settings_manager.core.settings_user import SettingsUser
from settings_manager.core.settings_script import SettingsScript
from settings_manager.core.schema_settings_type import SchemaSettingsType
from settings_manager.core.schema_settings import SchemaSettings

### Definition of the main scope
STRING_LIST_TYPE = Union[str, Iterable[str], None]
SCOPE_TYPE = Union[str, Scope]
SCHEMA_SETTINGSTYPE_TYPE = Union[str, SchemaSettingsType]
SCHEMA_SCOPE_TYPE = Union[str, SchemaScope]
SCHEMA_SETTINGS_TYPE = Union[str, SchemaSettings]
SCHEMA_SCOPE_LIST_TYPE = Union[str, SchemaScope, Iterable[Union[SchemaScope, str]], None]
SCOPE_LIST_TYPE = Union[str, Scope, Iterable[Union[Scope, str]], None]
SETTINGS_TYPE = Union[str, Settings]
PERMISSION_GROUP_TYPE = Union[str, PermissionGroup]
PERMISSION_GROUP_LIST_TYPE = Union[str, PermissionGroup, Iterable[Union[PermissionGroup, str]], None]
USER_TYPE = Union[str, SettingsUser]
USER_LIST_TYPE = Union[str, SettingsUser, Iterable[Union[SettingsUser, str]], None]
SCRIPT_TYPE = Union[str, SettingsUser]
SCRIPT_LIST_TYPE = Union[str, SettingsScript, Iterable[Union[SettingsScript, str]], None]