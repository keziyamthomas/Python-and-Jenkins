import pytest
from flask_app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    # Simulate a GET request to the root endpoint ('/')
    response = client.get('/')
    
    # Check if the status code is OK
    assert response.status_code == 200
    
    # Check if the returned string matches the expected one
    assert response.data == b"Hello There!"
	
