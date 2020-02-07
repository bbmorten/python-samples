
import requests
import json


# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "https://sandboxapicdc.cisco.com"


################## Get Hosts ##########################################################
# This function allows you to view a list of all the hosts in the network.
login_url = controller_url + '/api/aaaLogin.json'


payload = {
    "aaaUser":{
        "attributes":{
            "name":"admin",
            "pwd":"ciscopsdt"
        }
    }
}



# To create a policy, we need to use the POST method.
# When using POST, you need to specify the Content-Type header as application/json
headers = {'content-type': 'application/json'}


# Use requests.post to do a POST to the policy API
# Specify request body json data and headers
policy_create_response = requests.post(login_url, data=json.dumps(payload), headers=headers, verify=False)

print ("\nResult of Create" +  policy_create_response.text + '\n')


response = policy_create_response.json()

print(json.dumps(response, indent=4, separators=(',',': ')))

sessionToken = response["imdata"][0]["aaaLogin"]["attributes"]["token"]


tenant_url = controller_url + "/api/node/class/fvTenant.json"

sessionToken = 'APIC-cookie={}'.format(sessionToken)
#headers = {'content-type': 'application/json', 'Authorization': 'APIC-Cookie %s' % sessionToken}
#headers = {'content-type': 'application/json', 'access_Token' : sessionToken}
#headers = {'content-type': 'application/json', 'x-api-key' : sessionToken}
headers = {'content-type': 'application/json', 'Cookie' : sessionToken}

params = {'subscription' : 'yes'}

#get_req_response = requests.get(tenant_url, verify= False, headers=headers, params=params)
get_req_response = requests.get(tenant_url, verify= False, headers=headers)

response = get_req_response.json()

print(json.dumps(response, indent=4, separators=(',',': ')))



