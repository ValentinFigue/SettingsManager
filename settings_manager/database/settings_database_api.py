from settings_manager.database.settings_database import SettingsDatabase

from settings_manager.core.settings import Settings
from settings_manager.core.scope import Scope


class SettingsDatabaseAPI:

    def __init__(self, database: SettingsDatabase, identifier: str, password: str):

        self._database = database
        self._database.connect(identifier, password)

    def read(self, entity_type, entity_name, **filters):

        if entity_type is Settings:
            value = self._database.read_settings(entity_name, **filters)

        return value

    def create(self, entity_type, entity_name, **extra_fields):

        if entity_type is Settings:
            if 'scope' in extra_fields and 'entity_value' in extra_fields:
                value = self._database.create_settings(entity_name, entity_value=extra_fields['entity_value'],
                                                       scope=extra_fields['scope'])
            else:
                raise ValueError('Entity value and scope inputs must be sets')
        elif entity_type is Scope:
            if 'overridden_scopes' in extra_fields:
                value = self._database.create_scope(entity_name, overridden_scopes=extra_fields['overridden_scopes'])
            else:
                raise ValueError('overriden_scopes input must be sets')

        return value

    def update(self, entity_type, entity_name, entity_value, **filters):

        if entity_type is Settings:
            value = self._database.update_settings(entity_name, entity_value, **filters)

        return value

    def delete(self, entity_type, entity_name, **filters):

        if entity_type is Settings:
            value = self._database.delete_settings(entity_name, **filters)
        elif entity_type is Scope:
            value = self._database.delete_scope(entity_name)

        return value
