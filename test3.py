import requests
import pytest
from main3 import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    """Тест на успешный запрос и правильный URL."""
    mock_url = "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": mock_url}]

    mocker.patch("requests.get", return_value=mock_response)

    url = get_random_cat_image()
    assert url == mock_url

def test_get_random_cat_image_failure(mocker):
    """Тест на неуспешный запрос (например, статус код 404) и возврат None."""
    mock_url = "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

    mocker.patch("requests.get", return_value=mock_response)

    url = get_random_cat_image()
    assert url == None

if __name__ == "__main__":
    pytest.main()
