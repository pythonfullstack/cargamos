import json


def response_decode(response):
    return json.loads(response.data.decode())