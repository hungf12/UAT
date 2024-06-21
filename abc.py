import requests
import json
# Define the API endpoint
url = "https://chatbot-customers-mdw-uat.fpt.ai/api/v1/daiichi/client/policy-info"

# Define the data to send
data = {
    "Pol_ID": "002890615"
}

headers = {
    "Authorization": "uat-mdw-key-8888-8888-uat",
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, json=data,headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    json_fomat = json.dumps(data,ensure_ascii = False,indent = 4)
    # Print the data
    print(json_fomat)
else:
    print(f"Failed to post data: {response.status_code}")

json_point = json.loads(json_fomat)

'''
for key, value in json_point["set_attributes"].items():
    print(f"{key}: {value}")
'''

Bill_To_Date = json_point["set_attributes"]["Billed_To_Date"]
sundry_amt = json_point["set_attributes"]["Sundry_Amt"]
premium_unpaid = json_point["set_attributes"]["Target_Premium_Unpaid"]
if sundry_amt > premium_unpaid:
    print(f"true: {sundry_amt}")
else:
    print(f"false: {premium_unpaid}")
print(f"Billed_To_Date: {Bill_To_Date}")
