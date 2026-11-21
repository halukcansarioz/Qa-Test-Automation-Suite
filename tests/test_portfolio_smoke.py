from playwright.sync_api import Page, expect

BASE_URL = "https://halukcansarioz.github.io/"


def test_portfolio_returns_http_200(page: Page) -> None:
    response = page.goto(BASE_URL, wait_until="domcontentloaded")
    assert response is not None
    assert response.status == 200


def test_portfolio_title_contains_haluk(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    assert "Haluk" in page.title()


def test_portfolio_github_profile_link_exists(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    github_link = page.locator("a[href*='github.com']").first
    expect(github_link).to_be_attached()
  
