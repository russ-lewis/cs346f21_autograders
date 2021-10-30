#! /usr/bin/python3

import requests

r = requests.get("http://127.0.0.1/cgi-bin/school/courses")

print(f"Status: {r.status_code}")
print(f"Body (interpreted from JSON): {r.json()}")
print()

print("END TESTCASE")

