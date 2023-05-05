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
    def unregister_scope(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def check_scope_existence(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def parent_scope(self, scope_name: str, overridden_scope: str) -> bool:
        return

    @abstractmethod
    def unparent_scope(self, scope_name: str, overridden_scope: str) -> bool:
        return

    @abstractmethod
    def get_scopes_overridden_by(self, scope_name: str) -> SCOPE_LIST_TYPE:
        return

    @abstractmethod
    def get_scopes_that_overrides(self, scope_name: str) -> SCOPE_LIST_TYPE:
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

    def delete_scope(self, scope_name: str) -> bool:

        # Check the existence of the scope
        if not self.check_scope_existence(scope_name):
            return False

        # Loop over all the scopes that are overriden the scope that will be deleted
        for scope in self.get_scopes_overridden_by(scope_name):
            if not self.unparent_scope(scope_name, scope):
                return False
        # Loop over all the scopes that overrides the scope that will be deleted
        for scope in self.get_scopes_that_overrides(scope_name):
            if not self.unparent_scope(scope, scope_name):
                return False

        self.unregister_scope(scope_name)

        return True
