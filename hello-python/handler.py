import requests
import json
import os

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    #result = {"found": False}
    #json_req = json.loads(req)
    #r = requests.get(json_req["url"])
    #if json_req["term"] in r.text:
    #    result = {"found": True}

    #print json.dumps(result)
    #print("Hello! You said: " + req)
    print(os.environ['HOSTNAME']+", "+os.environ['configval'])
    #return req
