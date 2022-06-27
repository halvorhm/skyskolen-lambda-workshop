import json


def hello(event, context):
    body = {
        "message": "Dette er en personlig melding!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
