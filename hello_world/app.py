import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    def get_path_parameters(event):
        if (("pathParameters" in event)
                and (event["pathParameters"] is not None) 
                and ("proxy" in event["pathParameters"])):
            return event['pathParameters']['proxy'].split("/")
        elif (("rawPath" in event)
                and (event["rawPath"] is not None)):
            return event["rawPath"].split("/") 
        return "None"

    def get_query_string_parameters(event):
        if (("queryStringParameters" in event)
            and (event["queryStringParameters"] is not None)):
            return event["queryStringParameters"]
        return "None"

    html = f"""
        <html>
            <head>
                <title>Hello Univserse</title>
            </head>
        <body>
            <h1>Hello World</h1>
            <p>Path Parameters: {get_path_parameters(event)}</p>
            <p>Query String Parameters: {get_query_string_parameters(event)}</p>
            <p>{json.dumps(event)}</p>
        </body>
        </html>
        """


    return {
        "statusCode": 200,
        "body": html,
        "headers": {"Content-Type": "text/html"}
    }
    # application/json

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps(
    #         {
    #             "message": "hello world",
    #             "path" : event["path"],
    #             "event": event
    #             # "location": ip.text.replace("\n", "")
    #         }
    #     ),
    # }
