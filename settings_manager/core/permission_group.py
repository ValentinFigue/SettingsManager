class PermissionGroup:
    """
    Basic class defining a set of permissions
    """

    def __init__(self, name: str):
        """
        Basic Initialization
        """

        self._name = name
        self._users_list = None
        self._scripts_list = None

    def add_entity(self, user_name: str = None, script_name: str = None) -> bool:
        return True

    def remove_user(self, user_name: str = None, script_name: str = None) -> bool:
        return True
