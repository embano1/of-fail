def handle(event, context):
    print(event.body,flush=True)
    return {
        "statusCode": 400,
        "body": "I was programmed to fail"
    }
