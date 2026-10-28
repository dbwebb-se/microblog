"""
Test route for showing the version of the app, app/main/routes
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_default(client):
    """
    Test that the version is unknown when APP_VERSION is not set
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert response.data == b"unknown"



def test_version_set(client, test_app):
    """
    Test that the version is the value of APP_VERSION, without logging in
    """
    test_app.config["APP_VERSION"] = "11.0.1"
    response = client.get("/version")
    assert response.status_code == 200
    assert response.data == b"11.0.1"
