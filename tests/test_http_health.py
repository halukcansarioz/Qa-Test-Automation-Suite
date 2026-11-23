import pytest
import requests

TARGET_URL = "https://halukcansarioz.github.io/"


@pytest.fixture(scope="module")
def portfolio_response():
    response = requests.get(TARGET_URL, timeout=10)
    return response


def test_http_status_code_is_200(portfolio_response):
    assert portfolio_response.status_code == 200


def test_content_type_is_html(portfolio_response):
    content_type = portfolio_response.headers.get("Content-Type", "")
    assert "text/html" in content_type.lower()


def test_response_time_under_5_seconds(portfolio_response):
    assert portfolio_response.elapsed.total_seconds() < 5.0


def test_page_contains_author_name(portfolio_response):
    portfolio_response.encoding = "utf-8"
    assert "Haluk Can Sarıöz" in portfolio_response.text
