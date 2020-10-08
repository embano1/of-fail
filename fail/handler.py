counter = 0

def handle(event, context):
    global counter
    counter += 1

    print(event.body,flush=True)
    
    if counter == 3:
        # reset counter
        counter = 0
        return {
            "statusCode": 200,
            "body": f"I finally succeeded after {counter} attempts"
        }
        
    return {
        "statusCode": 500,
        "body": f"I was programmed to fail for the {counter} attempt"
    }
