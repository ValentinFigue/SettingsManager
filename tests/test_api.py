# External Import
import pytest

# Internal Import
from settings_manager.api.setting_manager_api import SettingsManagerAPI
from settings_manager.core.settings import Settings
from settings_manager.core.scope import Scope

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


@pytest.mark.parametrize('settings', ['test_settings', Settings('test_settings')])
def test_api_read_settings(settings_mock_database, settings):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    assert (settings_manager_api.read_settings(settings) is None)
    assert (settings_manager_api.update_settings(settings, 8))
    assert (settings_manager_api.read_settings(settings) == 8)
    assert (settings_manager_api.update_settings(settings, 4))
    assert (settings_manager_api.read_settings(settings) == 4)
    assert (settings_manager_api.delete_settings(settings))
    assert (settings_manager_api.read_settings(settings) is None)


def test_api_schema_modifications(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    assert (settings_manager_api.add_scope_to_database('Project', overridden_scopes=None))
    assert (settings_manager_api.add_scope_to_database('Sequence', overridden_scopes='Project'))
    assert (settings_manager_api.add_scope_to_database('Shot', overridden_scopes=['Sequence', Scope('Project')]))


