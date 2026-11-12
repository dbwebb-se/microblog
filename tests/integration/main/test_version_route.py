"""
Test version route
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_route_default(client):
    """
    Test version route with default value"""
    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'unknown'


def test_version_route_custom_value(client, test_app):
    """
    Test version route with custom value
    """
    test_app.config['APP_VERSION'] = '11.0.0'
    response = client.get('/version')

    assert response.status_code == 200
    assert response.data == b'11.0.0'
