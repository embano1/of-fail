def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    print(req)

    return { "statusCode": "500", "message": "I was programmed to fail" }
