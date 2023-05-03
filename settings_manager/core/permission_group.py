class PermissionGroup:
    """
    Basic class defining a set of permissions
    """

    def __init__(self, name):
        """
        Basic Initialization
        """

        self._name = name
        self._users_list = None
        self._scripts_list = None

    def add_entity(self, user_name=None, script_name=None):
        return

    def remove_user(self, user_name=None, script_name=None):
        return

