def handle(event, context):
    print(event.body,flush=True)
    return {
        "statusCode": 500,
        "body": "I was programmed to fail forever"
    }
