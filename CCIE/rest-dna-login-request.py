
import requests
import json
from requests.auth import HTTPBasicAuth

# DNA Center Doc URL is https://dcloud-dna-center-inst-sjc.cisco.com/dna/platform/app/consumer-portal/developer-toolkit/apis?apiId=ac8a-e94c-4e69-a09d


# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "https://dcloud-dna-center-inst-sjc.cisco.com"



################## Get Hosts ##########################################################
# This function allows you to view a list of all the hosts in the network.
login_url = controller_url + '/dna/system/api/v1/auth/token'

auth = HTTPBasicAuth('demo', 'demo1234!')
headers = {
    'Content-Type': 'application/json'
}

payload = {}



# Use requests.post to do a POST to the policy API
# Specify request body json data and headers
policy_create_response = requests.post(
    login_url, data=json.dumps(payload), headers=headers, auth=auth, verify=False)

print("\nResult of Create" + policy_create_response.text + '\n')


response = policy_create_response.json()

print(json.dumps(response, indent=4, separators=(',', ': ')))

