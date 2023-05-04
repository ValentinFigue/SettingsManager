from abc import ABC, abstractmethod

from settings_manager.core.settings_type import SettingsType
from settings_manager.constants.typing import SCOPE_TYPE
from settings_manager.constants.typing import SCOPE_LIST_TYPE


class SettingsDatabase(ABC):

    @abstractmethod
    def connect(self, identifier: str, password: str) -> bool:
        return True

    @abstractmethod
    def read_settings(self, settings_name: str, scope: SCOPE_TYPE) -> SettingsType:
        return

    @abstractmethod
    def create_settings(self, settings_name: str, entity_value: SettingsType, scope: SCOPE_TYPE) -> bool:
        return

    @abstractmethod
    def update_settings(self, settings_name: str, entity_value: SettingsType, scope: SCOPE_TYPE) -> bool:
        return

    @abstractmethod
    def delete_settings(self, settings_name: str, scope: SCOPE_TYPE) -> bool:
        return

    @abstractmethod
    def create_scope(self, scope_name: str, overridden_scopes: SCOPE_LIST_TYPE) -> bool:
        return
