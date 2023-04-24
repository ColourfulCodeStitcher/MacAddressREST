import argparse
import requests
import re


parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", required=True, nargs=1)
parser.add_argument("-a", "--address", required=True, nargs=1)
args = parser.parse_args()


def input_checker(address):
    match = re.search(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", address)
    if match:
        return True
    else:
        return False


def query_api(arguments):
    key = arguments.key[0]
    address = arguments.address[0]
    response = requests.get(f"https://api.macaddress.io/v1?apiKey={key}&output=vendor&search={address}")
    response_string = str(response.content)
    print(f"Returning vendor name: {response_string}")
    return response_string


def run(arguments):
    valid = input_checker(arguments.address[0])
    if valid:
        query_api(arguments)
    else:
        print("Invalid MAC address. Please try again")


run(args)