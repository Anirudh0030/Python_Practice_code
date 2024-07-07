import json
import os

def lambda_handler(event, context):
    # TODO implement
    my_variable_value = os.environ.get("MY_ENV_VARIABLE")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! with variable = '+my_variable_value)
    }