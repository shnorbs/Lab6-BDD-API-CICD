import base64, requests, allure

PLACEHOLDER_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
)

def before_scenario(context, scenario):
    context.created_ids = []

def after_step(context, step):
    if step.status.name == "failed":
        allure.attach(PLACEHOLDER_PNG, name="screenshot-on-failure",
                      attachment_type=allure.attachment_type.PNG)

def after_scenario(context, scenario):
    headers = getattr(context, "headers", None)
    for bin_id in context.created_ids:
        if headers:
            requests.delete(f"{context.base_url}/b/{bin_id}", headers=headers)