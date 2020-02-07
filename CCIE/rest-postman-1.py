import requests

url = "http://192.168.72.253/ins"

request_payload = "[\r\n  {\r\n    \"jsonrpc\": \"2.0\",\r\n    \"method\": \"cli\",\r\n    \"params\": {\r\n      \"cmd\": \"show interface\",\r\n      \"version\": 1\r\n    },\r\n    \"id\": 1\r\n  }\r\n]"
request_headers = {
  'Content-Type': 'application/json-rpc',
  'Authorization': 'Basic YWRtaW46MTEyMjMzb24h'
}

response = requests.request("POST", url, headers=request_headers, data = request_payload)

print(response.text.encode('utf8'))
