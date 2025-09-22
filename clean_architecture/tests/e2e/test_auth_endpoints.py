from fastapi.testclient import TestClient
from src.auth.model import RegisterUserRequest


def test_register_and_login_user(client: TestClient):
    register_data = RegisterUserRequest(
        email = "test.user@example.com",
        first_name = "Test",
        last_name= "User",
        password="testpassword123"
    )

    response = client.post("/auth/", json=register_data.model_dump())
    assert response.status_code == 201

    #Test Succesful login
    login_response = client.post("/auth/token", data={
        "username": register_data.email,
        "password" : register_data.password,
        "grant_type" : "password"
    })
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "access_token" in token_data
    assert token_data['token_type'] == "Bearer"



def test_login_failures(client: TestClient):
    response = client.post(
        "/auth/token",
        data={
            "username": "fake@example.com",
            "password": "wrongpassword",
            "grant_type": "password"
        }
    )

    assert response.status_code == 401

    #Test login with wrong password
    response = client.post(
        "/auth/token",
        data={
            "username": "test.user@example.com",
            "password" : "wrongpassword",
            "grant_type" : "password"
        }
    )

    assert response.status_code == 401

def test_rate_limiting(client: TestClient):
    #Test rate limiting on registration

    for _ in range(6):
        response = client.post(
            "/auth/",
            json = {
                "email": f"test{_}@example.com",
                "password": "testpassword123",
                "first_name": "Test",
                "last_name" : "User"
            }
        )

    assert response.status_code == 429 #Too many requests
