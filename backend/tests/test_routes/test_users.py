import json
from urllib import response

def test_user_signup(client):
  data = {"username": "largemouthbass", "email": "largemouth@bass.com", "password": "password", "home_lake_id": 1}
  response = client.post("/users/signup", json.dumps(data))
  assert response.status_code == 200
  assert response.json()["email"] == "largemouth@bass.com"
  assert response.json()["is_active"] == True