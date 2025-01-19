import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
       error12

def test_hello(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert json_data['message'] == 'Hello, NTT DATA!'
