import pytest
from app import app, db  # Import your Flask app and database instance

@pytest.fixture()
def test_client():
  app.config['TESTING'] = True  # Mark the app as in testing mode
  with app.test_client() as client:
    with app.app_context():
      db.create_all()  # Create necessary tables
    yield client 
    db.drop_all()  # Tear down the test database

def test_test_route(test_client):
  response = test_client.get('/test')  
  assert response.status_code == 200
  assert response.json == {'message': 'test route'}

def test_create_user(test_client):
  data = {'username': 'test_user', 'email': 'test@example.com'}
  response = test_client.post('/users', json=data) 
  assert response.status_code == 201
  assert response.json == {'message': 'user created'}
