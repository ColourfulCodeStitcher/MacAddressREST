# MacAddressREST
A simple RESTful API to query the company name of a MAC address

The script takes in 2 arguments in the command line:
- -k = user's API key
- -a = the MAC address to query

This isn't a fully fleshed-out command line tool yet, so will need to be run with "python3 main.py" and the relevant args

Checks that the input is a valid MAC address and queries the API to return the vendor name if it is valid

Lots of improvements to be made here:
- make into a command line tool rather than just a script
- returns a "b" in front of the response which needs getting rid of
- either improve the query function or add a new one to deal with other http responses (eg 4xx)
- make able to run in a docker container

Security: regex filters out anything that isn't a valid mac address to avoid malicious inputs