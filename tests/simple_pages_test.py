"""This test the homepage"""


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Satya" in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"GIT" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_oops(client):
    """This makes the index page"""
    response = client.get("/OOPS")
    assert response.status_code == 200
    assert b"OOP" in response.data


def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/AAA")
    assert response.status_code == 200
    assert b"AAA" in response.data


def test_request_caloop(client):
    """This makes the index page"""
    response = client.get("/CalOOP")
    assert response.status_code == 200
    assert b"Calculator" in response.data


def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/SOLID")
    assert response.status_code == 200
    assert b"SOLID" in response.data