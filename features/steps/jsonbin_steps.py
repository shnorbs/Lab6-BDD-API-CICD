import json, os, requests
from behave import given, when, then

@given('the JSONBin base URL is "{url}"')
def step_url(context, url):
    context.base_url = url.rstrip("/")

@given("I have a valid master key")
def step_key(context):
    key = os.environ.get("JSONBIN_MASTER_KEY")
    assert key, "JSONBIN_MASTER_KEY is not set"
    context.headers = {"X-Master-Key": key, "Content-Type": "application/json"}

def _create(context, payload):
    r = requests.post(f"{context.base_url}/b", headers=context.headers, data=payload)
    context.response = r
    if r.status_code == 200:
        context.bin_id = r.json()["metadata"]["id"]
        context.created_ids.append(context.bin_id)

@given("a bin exists with data '{payload}'")
def step_exists(context, payload):
    _create(context, payload)
    assert context.response.status_code == 200, context.response.text

@when("I create a bin with data '{payload}'")
def step_create(context, payload):
    _create(context, payload)

@when("I read the bin")
def step_read(context):
    context.response = requests.get(f"{context.base_url}/b/{context.bin_id}/latest", headers=context.headers)

@when("I delete the bin")
@given("I delete the bin")
def step_delete(context):
    context.response = requests.delete(f"{context.base_url}/b/{context.bin_id}", headers=context.headers)

@then("the response status code should be {code:d}")
def step_status(context, code):
    assert context.response.status_code == code, f"{context.response.status_code}: {context.response.text}"

@then("the response should contain a bin id")
def step_has_id(context):
    assert context.response.json()["metadata"]["id"]

@then("the record should equal '{expected}'")
def step_record(context, expected):
    assert context.response.json()["record"] == json.loads(expected)