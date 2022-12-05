import json
from urllib import response

# test_users - test for user signup
def test_user_signup(client):
  data = {"username": "largemouthbass", "email": "largemouth@bass.com", "password": "password"}
  response = client.post("/users/signup", json.dumps(data))
  assert response.status_code == 200
  assert response.json()["email"] == "largemouth@bass.com"
  assert response.json()["is_active"] == True