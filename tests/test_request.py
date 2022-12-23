
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


ipv4_1 = "1.2.3.4"
ipv4_2 = "1.2.3.5"
ipv6_1 = "2001:db8:0000:1:2:3:4:5"
ipv6_2 = "2001:db8::5"


def test_headers():
    response = client.get("/headers")
    assert response.status_code == 200
    assert response.json()["host"] == "testserver"


def test_ip():
    response = client.get("/ip")
    assert response.status_code == 200
    assert response.json()["ip"] == "testclient"
    assert "v4" in response.json()["message"][0]
    assert "graph" in response.json()["message"][1]

    response = client.get("/ip", headers = {"x-forwarded-for": ipv4_1})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv4_1

    response = client.get("/ip", headers = {"x-forwarded-for": ipv6_1})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv6_1

    response = client.get("/ip", headers = {"x-forwarded-for": ipv4_1, "fly-client-ip": ipv4_2})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv4_2

    response = client.get("/ip", headers = {"x-forwarded-for": ipv6_1, "fly-client-ip": ipv6_2})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv6_2


def test_ipv4():
    response = client.get("/ip/v4")
    assert response.status_code == 200
    assert response.json()["ip"] == "testclient"

    response = client.get("/ip/v4", headers = {"x-forwarded-for": ipv4_1})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv4_1

    response = client.get("/ip/v4", headers = {"x-forwarded-for": ipv4_1, "fly-client-ip": ipv4_2})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv4_2

    response = client.get("/ip/v4", headers = {"x-forwarded-for": ipv6_1})
    assert response.status_code == 422
    assert "IPv4" in response.json()["detail"]["message"]

    response = client.get("/ip/v4", headers = {"x-forwarded-for": ipv6_1, "fly-client-ip": ipv6_2})
    assert response.status_code == 422
    assert "IPv4" in response.json()["detail"]["message"]


def test_ipv6():

    response = client.get("/ip/v6")
    assert response.status_code == 422
    assert "IPv6" in response.json()["detail"]["message"]

    response = client.get("/ip/v6", headers = {"x-forwarded-for": ipv6_1})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv6_1

    response = client.get("/ip/v6", headers = {"x-forwarded-for": ipv6_1, "fly-client-ip": ipv6_2})
    assert response.status_code == 200
    assert response.json()["ip"] == ipv6_2

    response = client.get("/ip/v6", headers = {"x-forwarded-for": ipv4_1})
    assert response.status_code == 422
    assert "IPv6" in response.json()["detail"]["message"]

    response = client.get("/ip/v6", headers = {"x-forwarded-for": ipv4_1, "fly-client-ip": ipv4_2})
    assert response.status_code == 422
    assert "IPv6" in response.json()["detail"]["message"]


def test_user_agent():
    response = client.get("/user-agent")
    assert response.status_code == 200
    assert response.json()["user-agent"] == "testclient"


