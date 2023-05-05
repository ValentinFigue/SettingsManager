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

def test_api_schema_modifications_scope(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    # Scope Creation
    assert (settings_manager_api.add_schema_scope_to_database('Project'))
    assert (settings_manager_api.add_schema_scope_to_database('Shot', override=SchemaScope('Project')))
    assert (settings_manager_api.add_schema_scope_to_database('Sequence', override=SchemaScope('Project'), overridden_by='Shot'))
    assert (settings_mock_database.get_schema_scope_overridden_by('Sequence') == 'Project')
    assert (settings_mock_database.get_schema_scope_overridden_by('Shot') == 'Sequence')
    # Scope Deletion
    assert (settings_manager_api.delete_schema_scope_from_database('Sequence'))
    assert (settings_mock_database.get_schema_scope_overridden_by('Shot') == 'Project')


def test_api_schema_modifications_settings_type(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    # Settings Type Creation
    assert (settings_manager_api.add_schema_settings_type_to_database('Int', int))
    assert (settings_manager_api.add_schema_settings_type_to_database('Float', float))
    assert (settings_mock_database.check_schema_settings_type_existence('Float'))
    assert (not settings_mock_database.check_schema_settings_type_existence('float'))
    # Settings Type Deletion
    assert (settings_manager_api.delete_schema_settings_type_from_database('Int'))
    assert (not settings_mock_database.check_schema_settings_type_existence('Int'))


def test_api_schema_modifications_settings(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    # Setup Database
    settings_manager_api.add_schema_settings_type_to_database('Int', int)
    settings_manager_api.add_schema_settings_type_to_database('Str', str)
    settings_manager_api.add_schema_scope_to_database('Project')
    settings_manager_api.add_schema_scope_to_database('Shot', override=SchemaScope('Project'))
    settings_manager_api.add_schema_scope_to_database('Sequence', override=SchemaScope('Project'), overridden_by='Shot')
    # Settings Creation
    assert (settings_manager_api.add_schema_settings_to_database('Number', 'Int', [SchemaScope('Project'), 'Shot']))
    assert (settings_manager_api.add_schema_settings_to_database('Name', 'Str'))
    assert (not settings_manager_api.add_schema_settings_to_database('Name', 'Unknown'))
    # Settings Update
    assert (settings_manager_api.update_schema_settings_from_database('Name', 'Str', SchemaScope('Shot')))
    # Settings Deletion
    assert (settings_manager_api.delete_schema_settings_from_database('Name'))
    assert (not settings_mock_database.check_schema_settings_existence('Name'))


def test_api_scope_modifications(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    # Setup Database
    settings_manager_api.add_schema_scope_to_database('Project')
    settings_manager_api.add_schema_scope_to_database('Shot', override=SchemaScope('Project'))
    settings_manager_api.add_schema_scope_to_database('Sequence', override=SchemaScope('Project'), overridden_by='Shot')
    # Settings Creation
    assert (settings_manager_api.create_scope('test_project', 'Project'))
    assert (settings_manager_api.create_scope('test_shot', SchemaScope('Shot')))
    assert (not settings_manager_api.create_scope('test_project', 'Wrong scope'))
    # Settings Deletion
    assert (settings_manager_api.delete_scope('test_project', 'Project'))
    assert (not settings_manager_api.delete_scope('test_project', 'Sequence'))


def test_api_read_settings(settings_mock_database):
    settings_manager_api = SettingsManagerAPI(settings_mock_database, username='user_a', user_password='481')
    # Setup Database
    settings_manager_api.add_schema_scope_to_database('Project')
    settings_manager_api.add_schema_scope_to_database('Shot', override=SchemaScope('Project'))
    settings_manager_api.add_schema_scope_to_database('Sequence', override=SchemaScope('Project'), overridden_by='Shot')
    settings_manager_api.add_schema_settings_type_to_database('Int', int)
    settings_manager_api.add_schema_settings_type_to_database('Str', str)
    settings_manager_api.add_schema_settings_to_database('Number', 'Int', [SchemaScope('Project'), 'Sequence', 'Shot'])
    settings_manager_api.add_schema_settings_to_database('Number', 'Int', [SchemaScope('Project'), 'Shot'])
    settings_manager_api.create_scope('test_project', 'Project')
    settings_manager_api.create_scope('test_shot', SchemaScope('Shot'))
    settings_manager_api.create_scope('test_sequence', SchemaScope('Sequence'))
    # Create settings
    assert (settings_manager_api.create_settings('Number', 4, 'Project', 'test_project'))
    assert (settings_manager_api.create_settings('Number', 8, 'Shot', 'test_shot'))
