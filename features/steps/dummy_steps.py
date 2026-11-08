from behave import given, then, when
from playwright.sync_api import sync_playwright


LOGIN_URL = "http://webdriveruniversity.com/Login-Portal/index.html"
_playwright = None
_browser = None
_page = None


@given("I access the webdriver university login page")
def step_access_login_page(context):
    global _browser, _page, _playwright

    if _playwright is None:
        _playwright = sync_playwright().start()

    if _browser is None or not _browser.is_connected():
        _browser = _playwright.chromium.launch(headless=True)

    if _page is None or _page.is_closed():
        _page = _browser.new_page()

    context.page = _page
    context.page.goto(LOGIN_URL)


@given('I enter a username "{username}"')
def step_enter_username(context, username):
    context.page.locator("#text").fill(username)


@when('I enter a password "{password}"')
def step_enter_password(context, password):
    context.page.locator("#password").fill(password)


@when("I click on the login button")
def step_click_login(context):
    context.page.get_by_role("button", name="Login").click()


@then("I should be presented with the successful login message")
def step_verify_successful_login(context):
    assert context.page.url.endswith("/Login-Portal/run.html")


@then("I should be presented with the unsuccessful login message")
def step_verify_unsuccessful_login(context):
    assert context.page.url.endswith("/Login-Portal/fail.html")
