# External Import
import pytest

# Internal Import
from settings_manager.api.setting_manager_api import SettingsManagerAPI


#### INITIALIZATION ###

def test_api(settings_database_instance):
    settings_manager_api = SettingsManagerAPI(settings_database_instance)
    return

