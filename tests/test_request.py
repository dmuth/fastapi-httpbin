
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


ipv4_1 = "1.2.3.4"
ipv4_2 = "1.2.3.5"
ipv6_1 = "2001:db8:0000:1:2:3:4:5"
ipv6_2 = "2001:db8::5"


#
# Set up a fake request client
#
def setup_test_client(mocker):
    mock_client = mocker.patch("fastapi.Request.client")
    mock_client.host = "testclient"
    mock_client.port = "12345"


def test_headers(mocker):

    setup_test_client(mocker)

    response = client.get("/headers")
    assert response.status_code == 200
    assert response.json()["host"] == "testserver"


def test_ip(mocker):

    setup_test_client(mocker)

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


def test_ipv4(mocker):

    setup_test_client(mocker)

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


def test_ipv6(mocker):

    setup_test_client(mocker)

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


def test_user_agent(mocker):

    setup_test_client(mocker)

    response = client.get("/user-agent")
    assert response.status_code == 200
    assert response.json()["user-agent"] == "testclient"


