import pytest
# from flask_marshmallow import Marshmallow
from .istart_app import create_app
from .credentials import Credentials
from .config import Config

@pytest.fixture
def app():
    app = create_app(Config)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

