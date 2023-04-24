import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", required=True, nargs=1)
parser.add_argument("-a", "--address", required=True, nargs=1)
args = parser.parse_args()


def input_checker(arguments):
    # make condition to check if input is a valid MAC address
    # return True if valid, False if invalid
    pass


def query_api(arguments):
    # make query to the api here
    pass


def run(arguments):
    # call the other functions in here based on some conditions
    # still need to decide on a useful format for the output
    pass


run(args)