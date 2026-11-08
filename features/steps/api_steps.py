from behave import given, when, then
import requests

@given('the base URL is "{base_url}"')
def step_impl(context, base_url):
    context.base_url = base_url

@when('I send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    full_url = f"{context.base_url}{endpoint}"
    # Store the response in the context to use in the 'then' step
    context.response = requests.get(full_url)

@then('the response should contain "{expected_text}"')
def step_impl(context, expected_text):
    # Assert that the expected text is in the response body
    assert expected_text in context.response.text, \
    f"Response text did not contain '{expected_text}'. Actual text: '{context.response.text}'"

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    # Assert the HTTP status code
    assert context.response.status_code == status_code, \
    f"Expected status code {status_code} but got {context.response.status_code}"