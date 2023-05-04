# External Import
import pytest

# Internal Import
from settings_manager.api.setting_manager_api import SettingsManagerAPI


#### INITIALIZATION ###

def test_api_initialization(settings_mock_database):
    _ = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    _ = SettingsManagerAPI(settings_mock_database, script_name='script_a', script_key='481')
    try:
        _ = SettingsManagerAPI(settings_mock_database)
    except ValueError:
        pass
    else:
        assert False


def test_api_read_settings(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    assert (settings_manager_api.read_settings('test_settings') is None)
    assert (settings_manager_api.update_settings('test_settings', 8))
    assert (settings_manager_api.read_settings('test_settings') == 8)
    assert (settings_manager_api.update_settings('test_settings', 4))
    assert (settings_manager_api.read_settings('test_settings') == 4)
    assert (settings_manager_api.delete_settings('test_settings'))
    assert (settings_manager_api.read_settings('test_settings') is None)

