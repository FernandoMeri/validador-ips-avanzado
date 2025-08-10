Advanced IP Range Validator

Project Description
This Python script reads a text file with a list of IP addresses and classifies them as valid or invalid in a robust way. 
Unlike a basic validator, this script uses the `ipaddress` library to ensure that addresses comply with IPv4 format standards, including validation of numeric ranges (0-255).

Key Concepts
* ipaddress library (`ipaddress`): Used to validate and manipulate IP addresses efficiently and accurately.
* Error handling (`try-except`):Validation is performed by trying to create an IP address object. If the library throws an error (`ValueError`), the script catches it and classifies the IP as invalid.

How to Use the Script
1. Make sure you have the `ipaddress` library installed (`pip install ipaddress`).
2. Run the script in your terminal with `python validator.py`.

Results
The script will generate two output files:
* `ips_validates.txt`: Contains all IP addresses that comply with the standard.
* `ips_invalid.txt`: Contains the IP addresses that do not comply with the standard.

