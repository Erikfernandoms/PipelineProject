

def lambda_handler(event, context):
    message = "created with sucess"
    return {
        "statuscode": 200,
        "body": message
    }