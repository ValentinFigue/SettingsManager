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
    def get_scope_overridden_by(self, scope_name: str) -> SCOPE_TYPE:
        return

    @abstractmethod
    def get_scope_that_overrides(self, scope_name: str) -> SCOPE_TYPE:
        return

    """
    More complex functions that can be accomplished by manipulating the different operations above
    """

    def create_scope(self, scope_name: str, override: SCOPE_TYPE, overridden_by: SCOPE_TYPE,
                     replace_override=False) -> bool:

        # Check the existence of the scope
        if self.check_scope_existence(scope_name):
            return False
        # If not create it
        status_creation = self.register_scope(scope_name)
        if not status_creation:
            return False
        # Definition of the new overriden chain
        # In case we need to define a new scope that overrides
        if override is not None:
            print(type(override))
            # Get the scope that already overrides
            scope_already_overriding = self.get_scope_that_overrides(override)
            print(override)
            # Easy case
            if not scope_already_overriding:
                print(override)
                self.parent_scope(scope_name, override)
            # Check if it's the one that will override our new scope
            elif scope_already_overriding == overridden_by:
                # We can create a new chain with no conflict
                self.unparent_scope(scope_already_overriding, override)
                self.parent_scope(scope_name, override)
                self.parent_scope(overridden_by, scope_name)
                return True
            else:
                # In case of force mode
                if replace_override:
                    self.unparent_scope(scope_already_overriding, override)
                    self.parent_scope(scope_name, override)
                else:
                    return False
        # In case we need to define a new scope that is overriden
        if overridden_by is not None:
            # Get the scope that already overrides
            scope_already_overridden = self.get_scope_overridden_by(overridden_by)
            # Easy case
            if not scope_already_overridden:
                self.parent_scope(overridden_by, scope_name)
            elif scope_already_overridden != overridden_by:
                if replace_override:
                    self.unparent_scope(overridden_by, scope_already_overridden)
                    self.parent_scope(overridden_by, scope_name)
                else:
                    return False

        return True

    def delete_scope(self, scope_name: str) -> bool:

        # Check the existence of the scope
        if not self.check_scope_existence(scope_name):
            return False

        # Check if the scope is not a leaf
        scope_that_overrides = self.get_scope_that_overrides(scope_name)
        # Check if the scope is overridden
        scope_overridden_by = self.get_scope_overridden_by(scope_name)
        if scope_that_overrides and scope_overridden_by:
            # First unparent
            self.unparent_scope(scope_name, scope_overridden_by)
            self.unparent_scope(scope_that_overrides, scope_name)
            # Then parent the two remaining ones
            self.parent_scope(scope_that_overrides, scope_overridden_by)


        # Unregister of the scope
        self.unregister_scope(scope_name)

        return True
