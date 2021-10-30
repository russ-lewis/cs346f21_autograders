#! /usr/bin/python3

import requests

import os
os.system("bash setup_empty_server")


r = requests.get("http://127.0.0.1/cgi-bin/school/students")

print(f"Status: {r.status_code}")
print(f"Body (interpreted from JSON): {r.json()}")
print()

print("END TESTCASE")

