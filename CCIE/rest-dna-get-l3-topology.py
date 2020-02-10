
import requests
import json
from requests.auth import HTTPBasicAuth

def get_token(url):

    # Define API Call
    api_call = "/dna/system/api/v1/auth/token"

    # Payload contains authentication information
    payload = {}

    # Header information
    headers = {"content-type": "application/json"}
    auth = HTTPBasicAuth('demo', 'demo1234!')

    # Combine URL, API call and parameters variables
    url += api_call
    #url = url + api_call

    response = requests.post(url, json=payload, headers=headers, auth=auth, verify=False).json()

    # Return authentication token from respond body
    return response["Token"]

def get_l3topology(token, url, topology): 
    # Define API Call
    api_call = "/dna/intent/api/v1/topology/l3/{}".format(topology)


    # Header information
    headers = {"x-auth-token": token}

    # Combine URL, API call and parameters variables
    url += api_call

    print(url)
	
    response = requests.get(url, headers=headers, verify=False).json()
    
    # Get hosts list from response and return
    
    return response
    



# DNA Center Doc URL is https://dcloud-dna-center-inst-sjc.cisco.com/dna/platform/app/consumer-portal/developer-toolkit/apis?apiId=ac8a-e94c-4e69-a09d


# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# DNA Controller URL
controller_url = "https://dcloud-dna-center-inst-sjc.cisco.com"

authToken = get_token(controller_url)

print(authToken)

topology = get_l3topology(authToken,controller_url,"ospf")

print(topology)
