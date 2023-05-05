class Scope:

    def __init__(self, scope_name: str):

        self._scope_name = scope_name

    def __str__(self) -> str:

        return self._scope_name

    def __repr__(self) -> str:

        return self._scope_name
