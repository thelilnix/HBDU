import pytest
from HBDU import app as flask_app


# Change directory to `src/` then run `python -m pytest`

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def home_text():
    return b'HBDU - (Happy BirthDay U)'
