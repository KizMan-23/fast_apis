from fastapi.testclient import TestClient
from fastapi import status

def test_todo_crud_operations(client: TestClient, auth_headers):
    #Create Todo
    create_response = client.post(
        "/todos/",
        headers = auth_headers,
        json = {
            "title": "New Todo",
            "description" : "Testing Todo"
        }
    )
    assert create_response.status_code == 201
    todo_data = create_response.json()
    todo_id = todo_data['id']
    assert todo_data['description'] == "Testing Todo"
    assert not todo_data['is_completed']

    #Get All Todos
    list_response = client.get(
        "/todos/",
        headers=auth_headers)
    
    assert list_response.status_code == 200
    todos = list_response.json()
    assert len(todos) > 0
    assert any(todo["id"] == todo_id for todo in todos)

    #Get Specific todo
    get_response = client.get(f"/todos/{todo_id}", headers=auth_headers)
    assert get_response.status_code == status.HTTP_200_OK
    assert get_response.json()['id'] == todo_id

    #Update Todo
    update_response = client.put(f"/todos/{todo_id}", headers=auth_headers,
    json={
        "title": "Updated Title",
        "description": "Updated New Todo"})
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data['title'] == "Updated Title"
    assert updated_data['description'] == "Updated New Todo"

    #Completed todo
    complete_response = client.put(f"/todos/{todo_id}/complete", headers=auth_headers)
    assert complete_response.status_code == 200
    assert complete_response.json()['is_completed']

    #delete todo
    delete_response = client.delete(f"/todos/{todo_id}", headers=auth_headers)
    assert delete_response.status_code == 204

    #verify delete
    get_delete_response = client.get(f"/todos/{todo_id}", headers=auth_headers)
    assert get_delete_response.status_code == 404


def test_todo_authorizatioin(client: TestClient, auth_headers):
    #Create New Todo
    create_response = client.post(
        '/todos/',
        headers=auth_headers,
        json = {
            "title": "New Auth Todo",
            "description" : "Testing Todo Authorization"
        }
    )
    assert create_response.status_code == 201
    todo_id = create_response.json()['id']

    #Try accesssing Todo without Auth
    endpoints = [
        ("GET", f"/todos/"),
        ("GET", f"/todos/{todo_id}"),
        ("POST", f"/todos/"),
        ("PUT", f"/todos/{todo_id}"),
        ("PUT", f"/todos/{todo_id}/complete"),
        ("DELETE", f"/todos/{todo_id}")
    ]

    for method, endpoint in endpoints:
        response = client.request(method, endpoint)
        assert response.status_code == 401

    