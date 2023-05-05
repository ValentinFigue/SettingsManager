# External Import
import pytest

# Internal Import
from settings_manager.api.setting_manager_api import SettingsManagerAPI
from settings_manager.core.settings import Settings
from settings_manager.core.schema_scope import SchemaScope

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


def test_api_schema_modifications_scope(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    # Scope Creation
    assert (settings_manager_api.add_scope_to_database('Project'))
    assert (settings_manager_api.add_scope_to_database('Shot', override=SchemaScope('Project')))
    assert (settings_manager_api.add_scope_to_database('Sequence', override=SchemaScope('Project'), overridden_by='Shot'))
    assert (settings_mock_database.get_schema_scope_overridden_by('Sequence') == 'Project')
    assert (settings_mock_database.get_schema_scope_overridden_by('Shot') == 'Sequence')
    # Scope Deletion
    assert (settings_manager_api.delete_scope_from_database('Sequence'))
    assert (settings_mock_database.get_schema_scope_overridden_by('Shot') == 'Project')


