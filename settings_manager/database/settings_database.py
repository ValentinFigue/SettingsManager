from abc import ABC, abstractmethod

from settings_manager.core.settings_type import SettingsType
from settings_manager.core.scope import Scope
from settings_manager.constants.typing import SCOPE_TYPE
from settings_manager.constants.typing import SCOPE_LIST_TYPE


class SettingsDatabase(ABC):

    """
    Basic functions that need to be overridden by the different database implementations depending on how you want to
    register the information
    """

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
    def register_scope(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def check_scope_existence(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def parent_scope(self, scope_name: str, overridden_scope: str) -> bool:
        return

    """
    More complex functions that can be accomplished by manipulating the different operations above
    """

    def create_scope(self, scope_name: str, overridden_scopes: SCOPE_LIST_TYPE) -> bool:

        # Check the existence of the scope
        if self.check_scope_existence(scope_name):
            return False
        # If not create it
        status_creation = self.register_scope(scope_name)
        if not status_creation:
            return False
        # Loop over all the scopes that will be overriden
        if overridden_scopes:
            if isinstance(overridden_scopes, (str, Scope)):
                self.parent_scope(scope_name, overridden_scopes)
            else:
                for overridden_scope in overridden_scopes:
                    self.parent_scope(scope_name, overridden_scope)
        return True

