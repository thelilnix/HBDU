from HBDU.views import THEMES


def test_home(client, home_text):
    response = client.get('/')
    assert response.status_code == 200
    assert home_text in response.data


def test_say_happy(client, home_text):
    post_data = {
        "name": "Friend's name",
        "author": "My name",
        "theme": "Birthday_1"
    }

    for theme in THEMES:
        post_data["theme"] = theme
        response = client.post(
            '/v1/say_happy',
            data=post_data,
            follow_redirects=True
        )
        assert response.status_code == 200
        assert home_text not in response.data

    post_data["theme"] = "Birthday_wrong_index"
    response = client.post(
        '/v1/say_happy',
        data=post_data,
        follow_redirects=True
    )
    assert response.status_code == 200
    assert home_text in response.data


def test_handle_theme(client):
    for theme in THEMES:
        response = client.get(f"/v1/themes/{theme}/friend/author")
        assert response.status_code == 200

    response = client.get("/v1/themes/friend/author/WRONG_theme")
    assert response.status_code == 302


def test_error_404(client):
    response = client.get('/donno_nowhere')
    assert response.status_code == 404
