# External Import
import pytest

# Internal Import
from settings_manager.api.setting_manager_api import SettingsManagerAPI


#### INITIALIZATION ###

def test_api_initialization(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    return

