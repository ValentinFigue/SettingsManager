from settings_manager.database.settings_database import SettingsDatabase

from settings_manager.core.settings import Settings
from settings_manager.core.schema_scope import SchemaScope
from settings_manager.core.schema_settings_type import SchemaSettingsType
from settings_manager.core.schema_settings import SchemaSettings

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
                raise ValueError('Entity value and scope inputs must be set')
        elif entity_type is SchemaScope:
            if 'override' in extra_fields and 'overridden_by' in extra_fields and 'replace_override' in extra_fields:
                value = self._database.create_schema_scope(entity_name,
                                                           override=extra_fields['override'],
                                                           overridden_by=extra_fields['overridden_by'],
                                                           replace_override=extra_fields['replace_override'])
            else:
                raise ValueError('overriden_scopes input must be set')
        elif entity_type is SchemaSettingsType:
            if 'settings_type' in extra_fields:
                value = self._database.create_schema_settings_type(entity_name,
                                                                   settings_type=extra_fields['settings_type'])
            else:
                raise ValueError('settings_type input must be set')
        elif entity_type is SchemaSettings:
            if 'schema_settings_type' in extra_fields and 'schema_scopes' in extra_fields \
                    and 'permissions_groups' in extra_fields:
                value = self._database.create_schema_settings(entity_name,
                                                              schema_settings_type=extra_fields['schema_settings_type'],
                                                              schema_scopes=extra_fields['schema_scopes'],
                                                              permissions_groups=extra_fields['permissions_groups']
                                                              )
            else:
                raise ValueError('settings_type input must be set')

        return value

    def update(self, entity_type: object, entity_name: str, **extra_fields):

        if entity_type is Settings:
            if 'entity_value' in extra_fields and 'scope' in extra_fields:
                value = self._database.update_settings(entity_name,
                                                       entity_value=extra_fields['entity_value'],
                                                       scope=extra_fields['scope'])
            else:
                raise ValueError('entity_value input must be set')
        elif entity_type is SchemaSettings:
            if 'schema_settings_type' in extra_fields and 'schema_scopes' in extra_fields \
                    and 'permissions_groups' in extra_fields:
                value = self._database.update_schema_settings(entity_name,
                                                              schema_settings_type=extra_fields['schema_settings_type'],
                                                              schema_scopes=extra_fields['schema_scopes'],
                                                              permissions_groups=extra_fields['permissions_groups']
                                                              )
            else:
                raise ValueError('settings_type input must be set')

        return value

    def delete(self, entity_type, entity_name, **filters):

        if entity_type is Settings:
            value = self._database.delete_settings(entity_name, **filters)
        elif entity_type is SchemaScope:
            value = self._database.delete_schema_scope(entity_name)
        elif entity_type is SchemaSettingsType:
            value = self._database.delete_schema_settings_type(entity_name)
        elif entity_type is SchemaSettings:
            value = self._database.delete_schema_settings(entity_name)

        return value
