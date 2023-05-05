from abc import ABC, abstractmethod
from typing import Any

from settings_manager.core.schema_settings_type import SchemaSettingsType
from settings_manager.constants.typing import SCOPE_TYPE
from settings_manager.constants.typing import SCHEMA_SCOPE_TYPE
from settings_manager.constants.typing import STRING_LIST_TYPE
from settings_manager.constants.typing import SCHEMA_SCOPE_LIST_TYPE

class SettingsDatabase(ABC):

    """
    Basic functions that need to be overridden by the different database implementations depending on how you want to
    register the information
    """

    @abstractmethod
    def connect(self, identifier: str, password: str) -> bool:
        return True

    @abstractmethod
    def get_settings(self, settings_name: str, scope: str, schema_scope: str) -> Any:
        return

    @abstractmethod
    def set_settings(self, settings_name: str, entity_value: Any, scope: str, schema_scope: str) -> bool:
        return

    @abstractmethod
    def register_settings(self, settings_name: str, entity_value: Any, scope: str, schema_scope: str) -> bool:
        return

    @abstractmethod
    def register_settings(self, settings_name: str, entity_value: Any, scope: str, schema_scope: str) -> bool:
        return

    @abstractmethod
    def unregister_settings(self, settings_name: str, scope: str, schema_scope: str) -> bool:
        return

    @abstractmethod
    def check_settings_existence(self, settings_name: str, scope_name: str, schema_scope: str) -> bool:
        return

    @abstractmethod
    def register_schema_scope(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def unregister_schema_scope(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def check_schema_scope_existence(self, scope_name: str) -> bool:
        return

    @abstractmethod
    def parent_schema_scope(self, scope_name: str, overridden_scope: str) -> bool:
        return

    @abstractmethod
    def unparent_schema_scope(self, scope_name: str, overridden_scope: str) -> bool:
        return

    @abstractmethod
    def get_schema_scope_overridden_by(self, scope_name: str) -> SCHEMA_SCOPE_TYPE:
        return

    @abstractmethod
    def get_schema_scope_that_overrides(self, scope_name: str) -> SCHEMA_SCOPE_TYPE:
        return

    @abstractmethod
    def register_schema_settings_type(self, settings_type_name: str, settings_type: type) -> bool:
        return

    @abstractmethod
    def unregister_schema_settings_type(self, settings_type_name: str) -> bool:
        return

    @abstractmethod
    def check_schema_settings_type_existence(self, settings_type_name: str) -> bool:
        return

    @abstractmethod
    def register_schema_settings(self, settings_name: str, schema_settings_type: str,
                                 schema_scopes:  STRING_LIST_TYPE, permissions_groups:  STRING_LIST_TYPE) -> bool:
        return

    @abstractmethod
    def unregister_schema_settings(self, settings_name: str) -> bool:
        return

    @abstractmethod
    def set_schema_settings(self, settings_name: str, schema_settings_type: str,
                            schema_scopes:  STRING_LIST_TYPE, permissions_groups:  STRING_LIST_TYPE) -> bool:
        return

    @abstractmethod
    def check_schema_settings_existence(self, settings_name: str) -> bool:
        return

    @abstractmethod
    def check_scope_existence(self, scope_name: str, schema_scope_name: str) -> bool:
        return

    @abstractmethod
    def register_scope(self, scope_name: str, schema_scope_name: str) -> bool:
        return

    @abstractmethod
    def unregister_scope(self, scope_name: str, schema_scope_name: str) -> bool:
        return

    @abstractmethod
    def get_settings_type(self, settings_name: str) -> type:
        return

    @abstractmethod
    def get_settings_scope(self, settings_name: str) -> SCHEMA_SCOPE_LIST_TYPE:
        return


    """
    More complex functions that can be accomplished by manipulating the different operations above
    """

    def create_schema_scope(self, scope_name: str, override: SCOPE_TYPE, overridden_by: SCOPE_TYPE,
                            replace_override=False) -> bool:

        # Check the existence of the scope
        if self.check_schema_scope_existence(scope_name):
            return False
        # If not create it
        status_creation = self.register_schema_scope(scope_name)
        if not status_creation:
            return False
        # Definition of the new overriden chain
        # In case we need to define a new scope that overrides
        if override is not None:
            # Get the scope that already overrides
            scope_already_overriding = self.get_schema_scope_that_overrides(override)
            # Easy case
            if not scope_already_overriding:
                self.parent_schema_scope(scope_name, override)
            # Check if it's the one that will override our new scope
            elif scope_already_overriding == overridden_by:
                # We can create a new chain with no conflict
                self.unparent_schema_scope(scope_already_overriding, override)
                self.parent_schema_scope(scope_name, override)
                self.parent_schema_scope(overridden_by, scope_name)
                return True
            else:
                # In case of force mode
                if replace_override:
                    self.unparent_schema_scope(scope_already_overriding, override)
                    self.parent_schema_scope(scope_name, override)
                else:
                    return False
        # In case we need to define a new scope that is overriden
        if overridden_by is not None:
            # Get the scope that already overrides
            scope_already_overridden = self.get_schema_scope_overridden_by(overridden_by)
            # Easy case
            if not scope_already_overridden:
                self.parent_schema_scope(overridden_by, scope_name)
            elif scope_already_overridden != overridden_by:
                if replace_override:
                    self.unparent_schema_scope(overridden_by, scope_already_overridden)
                    self.parent_schema_scope(overridden_by, scope_name)
                else:
                    return False

        return True

    def delete_schema_scope(self, scope_name: str) -> bool:

        # Check the existence of the scope
        if not self.check_schema_scope_existence(scope_name):
            return False

        # Check if the scope is not a leaf
        scope_that_overrides = self.get_schema_scope_that_overrides(scope_name)
        # Check if the scope is overridden
        scope_overridden_by = self.get_schema_scope_overridden_by(scope_name)
        if scope_that_overrides and scope_overridden_by:
            # First unparent
            self.unparent_schema_scope(scope_name, scope_overridden_by)
            self.unparent_schema_scope(scope_that_overrides, scope_name)
            # Then parent the two remaining ones
            self.parent_schema_scope(scope_that_overrides, scope_overridden_by)

        # Unregister of the scope
        self.unregister_schema_scope(scope_name)

        return True

    def create_schema_settings_type(self, settings_type_name: str, settings_type: type) -> bool:

        # Check existence of schema settings type
        if self.check_schema_settings_type_existence(settings_type_name):
            return False

        return self.register_schema_settings_type(settings_type_name, settings_type)

    def delete_schema_settings_type(self, settings_type_name: str) -> bool:

        # Check existence of schema settings type
        if not self.check_schema_settings_type_existence(settings_type_name):
            return False

        # TODO: Check if some settings are using this type

        return self.unregister_schema_settings_type(settings_type_name)

    def create_schema_settings(self, settings_name: str, schema_settings_type: str,
                               schema_scopes:  STRING_LIST_TYPE, permissions_groups:  STRING_LIST_TYPE) -> bool:

        # Check existence of the schema settings
        if self.check_schema_settings_existence(settings_name):
            return False

        # Check that settings type exists
        if not self.check_schema_settings_type_existence(schema_settings_type):
            return False

        # Check that all scopes exist
        for scope in schema_scopes:
            if not self.check_schema_scope_existence(scope):
                return False

        # TODO: Do the same with the permissions
        self.register_schema_settings(settings_name, schema_settings_type, schema_scopes, permissions_groups)

        return True

    def delete_schema_settings(self, settings_name: str) -> bool:

        # Check existence of the schema settings
        if not self.check_schema_settings_existence(settings_name):
            return False

        # TODO: Check that no settings are depending from this schema

        self.unregister_schema_settings(settings_name)

        return True

    def update_schema_settings(self, settings_name: str, schema_settings_type: str,
                               schema_scopes: STRING_LIST_TYPE, permissions_groups: STRING_LIST_TYPE) -> bool:

        # Check existence of the schema settings
        if not self.check_schema_settings_existence(settings_name):
            return False

        # Check that settings type exists
        if not self.check_schema_settings_type_existence(schema_settings_type):
            return False

        # Check that all scopes exist
        for scope in schema_scopes:
            if not self.check_schema_scope_existence(scope):
                return False

        # TODO: Do the same with the permissions
        self.set_schema_settings(settings_name, schema_settings_type, schema_scopes, permissions_groups)

        return True

    def create_scope(self, scope_name: str, schema_scope: str) -> bool:

        # Check existence of the schema scope
        if not self.check_schema_scope_existence(schema_scope):
            return False

        # Check existence of the scope
        if self.check_scope_existence(scope_name, schema_scope):
            return False

        self.register_scope(scope_name, schema_scope)

        return True

    def delete_scope(self, scope_name: str, schema_scope: str) -> bool:

        # Check existence of the schema scope
        if not self.check_schema_scope_existence(schema_scope):
            return False

        # Check existence of the scope
        if not self.check_scope_existence(scope_name, schema_scope):
            return False

        self.unregister_scope(scope_name, schema_scope)

        return True

    def create_settings(self, settings_name: str, settings_value: Any, scope_name: str, schema_scope: str) -> bool:

        # Check existence of the schema scope
        if not self.check_schema_scope_existence(schema_scope):
            return False

        # Check existence of the scope
        if not self.check_scope_existence(scope_name, schema_scope):
            return False

        # Check existence of the settings name
        self.check_schema_settings_existence(settings_name)

        # Get type of the settings_name
        settings_type = self.get_settings_type(settings_name)
        # Check that the settings value to fill is conform to the settings type
        if not isinstance(settings_value, settings_type):
            return False

        # Check that the scope is compatible
        settings_scopes = self.get_settings_scope(settings_name)
        if schema_scope not in settings_scopes:
            return False

        # Check that the settings does not exist
        if self.check_settings_existence(settings_name, scope_name, schema_scope):
            return False

        self.register_settings(settings_name, settings_value, scope_name, schema_scope)

        return True

    def delete_settings(self, settings_name: str, scope_name: str, schema_scope: str) -> bool:

        # Check existence of the schema scope
        if not self.check_schema_scope_existence(schema_scope):
            return False

        # Check existence of the scope
        if not self.check_scope_existence(scope_name, schema_scope):
            return False

        # Check existence of the settings name
        self.check_schema_settings_existence(settings_name)

        # Check that the scope is compatible
        settings_scopes = self.get_settings_scope(settings_name)
        if schema_scope not in settings_scopes:
            return False

        # Check that the settings does not exist
        if not self.check_settings_existence(settings_name, scope_name, schema_scope):
            return True

        self.unregister_settings(settings_name, scope_name, schema_scope)

        return True

    def update_settings(self, settings_name: str, settings_value: Any, scope_name: str, schema_scope: str) -> bool:

        # Check existence of the schema scope
        if not self.check_schema_scope_existence(schema_scope):
            return False

        # Check existence of the scope
        if not self.check_scope_existence(scope_name, schema_scope):
            return False

        # Check existence of the settings name
        self.check_schema_settings_existence(settings_name)

        # Check that the scope is compatible
        settings_scopes = self.get_settings_scope(settings_name)
        if schema_scope not in settings_scopes:
            return False

        # Get type of the settings_name
        settings_type = self.get_settings_type(settings_name)
        # Check that the settings value to fill is conform to the settings type
        if not isinstance(settings_value, settings_type):
            return False

        # Check that the settings does not exist
        if not self.check_settings_existence(settings_name, scope_name, schema_scope):
            return True

        self.set_settings(settings_name, settings_value, scope_name, schema_scope)

        return True

    def read_settings(self, settings_name: str, **scope_filters) -> Any:

        # Check existence of the scopes provided in the filters and remove the ones that does not exist or not linked
        # to the settings
        settings_scopes = self.get_settings_scope(settings_name)

        for scope_schema in scope_filters.copy().keys():
            if scope_schema not in settings_scopes or not self.check_schema_scope_existence(scope_schema):
                del scope_filters[scope_schema]

        # Reconstruct the chain of dependency
        # Start from a random scope
        initial_scope = list(scope_filters.keys())[0]
        ordered_chain = []
        ordered_chain.append(initial_scope)
        # Get lower scopes
        lower_level_scope = self.get_schema_scope_overridden_by(initial_scope)
        while lower_level_scope is not None:
            ordered_chain.append(lower_level_scope)
            lower_level_scope = self.get_schema_scope_overridden_by(lower_level_scope)
        # Get higher scopes
        higher_level_scope = self.get_schema_scope_that_overrides(initial_scope)
        while higher_level_scope is not None:
            ordered_chain.insert(0, higher_level_scope)
            higher_level_scope = self.get_schema_scope_that_overrides(higher_level_scope)

        # Check that all scopes are in the override chain
        for scope in scope_filters.keys():
            if scope not in ordered_chain:
                print('Impossible to find a settings due to different override chains')
                return None
        # Remove from the ordered chain the non matching filters
        for scope in ordered_chain.copy():
            if scope not in scope_filters.keys():
                ordered_chain.remove(scope)

        # Try to get the highest override settings
        for scope in ordered_chain:
            if self.check_settings_existence(settings_name, scope_name=scope_filters[scope],
                                             schema_scope=scope):
                return self.get_settings(settings_name, schema_scope=scope,
                                         scope=scope_filters[scope])

        return None
