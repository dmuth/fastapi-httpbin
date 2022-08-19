
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_cookies():

    response = client.get("/cookies")
    assert response.status_code == 200
    assert len(response.cookies) == 0
    assert response.json()["message"] == "0 cookies seen in request."

    cookies = {}
    response = client.put("/cookies", json = cookies)
    assert response.status_code == 200
    assert len(response.cookies) == 0
    assert response.json()["message"] == "0 cookies set in response."

    cookies = {"cookie1": "value1"}
    response = client.put("/cookies", json = cookies)
    assert response.status_code == 200
    assert len(response.cookies) == 1
    assert response.json()["message"] == "1 cookie set in response."
 
    cookies = {"cookie1": "value1", "cookie2": "value2", "cookie3": "value3"}
    response = client.put("/cookies", json = cookies)
    assert response.status_code == 200
    assert len(response.cookies) == 3
    assert response.json()["message"] == "3 cookies set in response."
 
    response = client.get("/cookies")
    assert response.status_code == 200
    assert len(response.cookies) == 3
    assert response.json()["message"] == "3 cookies seen in request."
   
    cookies = ["cookie1"]
    response = client.delete("/cookies", json = cookies)
    assert response.status_code == 200
    assert response.json()["message"] == "1 cookie deleted."
    
    response = client.get("/cookies")
    assert response.status_code == 200
    assert len(response.cookies) == 2
    assert response.json()["message"] == "2 cookies seen in request."

    cookies = ["cookie2", "cookie3", "cookie4"]
    response = client.delete("/cookies", json = cookies)
    assert response.status_code == 200
    assert response.json()["message"] == "2 cookies deleted."
    
    cookies = ["cookie2", "cookie3", "cookie4"]
    response = client.delete("/cookies", json = cookies)
    assert response.status_code == 200
    assert response.json()["message"] == "0 cookies deleted."
    
    response = client.get("/cookies")
    assert response.status_code == 200
    assert len(response.cookies) == 0
    assert response.json()["message"] == "0 cookies seen in request."


