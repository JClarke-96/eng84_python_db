# API for postcode.io

import requests

url = "http://api.postcodes.io/postcodes/"
postcode = "e147le"

url_arg = url + postcode
print(url_arg)

response = requests.get(url_arg)

print(response.status_code)
response_dict = response.json()
for key in response_dict.keys():
    if key == "result":
        print(f"Postcode is {response_dict[key]['postcode']}")
print(response_dict)
