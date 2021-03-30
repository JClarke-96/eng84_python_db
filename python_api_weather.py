# API for bbc.co.uk

import requests


def postcode_info():
    print("Hello, welcome to Postcode info")
    postcode_input = input("Please enter a postcode: ")
    return postcode_input


def connection(postcode):
    url = "http://api.postcodes.io/postcodes/"
    url_arg = url + postcode
    print(url_arg)
    return requests.get(url_arg)


def info(response):
    response_dict = response.json()
    for key in response_dict.keys():
        if key == "result":
            print(f"Postcode is {response_dict[key]['postcode']}")
            print(f"Country is {response_dict[key]['country']}")
            print(f"Location is {response_dict[key]['admin_district']}")


postcode = postcode_info()
response = connection(postcode)
print(response.status_code)
info(response)
