import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", required=True, nargs=1)
parser.add_argument("-a", "--address", required=True, nargs=1)
args = parser.parse_args()


def input_checker(address):
    # make condition to check if input is a valid MAC address
    # return True if valid, False if invalid
    pass


def query_api(arguments):
    response = requests.get(f"https://api.macaddress.io/v1?apiKey={arguments.key}&output=json&search={arguments.address}")
    # TODO: format response from JSON to useful format - just a string?
    pass


def run(arguments):
    valid = inputchecker(arguments.address)
    if valid:
        query_api(arguments)
    else:
        print("Invalid MAC address. Please try again")


run(args)