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
    response = requests.get(f"https://api.macaddress.io/v1?apiKey={arguments.key}&output=vendor&search={arguments.address}")
    print(f"Returning vendor name: {response}")
    return response


def run(arguments):
    valid = inputchecker(arguments.address)
    if valid:
        query_api(arguments)
    else:
        print("Invalid MAC address. Please try again")


run(args)