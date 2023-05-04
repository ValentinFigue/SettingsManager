import pytest

from settings_manager.implementation.mock_database import MockDatabase

@pytest.fixture
def settings_mock_database():
    return MockDatabase()
