class SchemaSettingsType:

    def __init__(self, settings_type: type, settings_type_name: str):

        self._settings_type = settings_type
        self._settings_type_name = settings_type_name

    def __str__(self):

        return self._settings_type_name