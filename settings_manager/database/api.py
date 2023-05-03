class SettingsDatabaseAPI():

    def __init__(self, instance: str):

        self.connect(instance)

    def connect(self, instance: str) -> bool:
        return True

    def read(self, entity_type, entity_name, filters):
        value = None
        return value

    def create(self, entity_type, entity_name, entity_value, extra_fields):
        return True

    def update(self, entity_type, entity_name, entity_value, filters):
        return True

    def delete(self, entity_type, entity_name, filters):
        return True
