class Settings_Manager_API:
    def __init__(self, instance, username=None, script_name=None, password=None):

        self._instance = instance
        self._username = username
        self._script_name = script_name
        self._password = password

    def read(self, settings_name, scope=None):
        return

    def update(self, settings_name, value, scope=None):
        return

    def delete(self, settings_name, scope=None):
        return

    def create(self, settings_name, settings_type, scope=None):
        return
