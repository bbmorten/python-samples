import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('admin', '112233on!')
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show interface",
            "output_format": "json"
        }
    }
    url = 'http://192.168.72.253/ins'

    response = requests.post(url, data=json.dumps(payload),
                         headers=headers, auth=auth)

    print(response.status_code)
    print(response.headers)
    #print(response.text)
    # Response.text --> JSON String

    # Json.loads JSON string'i --> Dictionary
    output = json.loads(response.text)
    print(output)