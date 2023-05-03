class SettingsManagerAPI:
    def __init__(self, instance, username=None, script_name=None, password=None):

        self._instance = instance
        self._username = username
        self._script_name = script_name
        self._password = password

    """
    CRUD functions to directly read and update settings data
    """

    def read(self, settings_name, scope=None):
        return

    def update(self, settings_name, value, scope=None):
        return

    def delete(self, settings_name, scope=None):
        return

    def create(self, settings_name, settings_type, scope=None):
        return

    """
    CRUD functions to directly update settings database schema
    """

    def add_scope(self, scope_name, overridden_scopes=None):
        return

    def delete_scope(self, scope_name):
        return

    def add_settings(self, settings_name, settings_type, scopes=None, permissions_groups=None):
        return

    def update_settings(self, settings_name, settings_type, scopes=None, permission_groups=None):
        return

    def delete_settings(self, settings_name):
        return

    def add_permission_group(self, permission_group_name, users=None, scripts=None):
        return

    def update_permission_group(self, permission_group_name, users=None, scripts=None):
        return

    def delete_permission_group(self, permission_group_name, users=None, scripts=None):
        return

    def add_user(self, user_name, permission_group=None):
        return

    def delete_user(self, user_name):
        return

    def add_script(self, script_name, permission_group=None):
        return

    def delete_script(self, script_name):
        return
