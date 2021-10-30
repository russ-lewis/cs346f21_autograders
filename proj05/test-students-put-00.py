#! /usr/bin/python3

import requests
import json


def crop_location(loc):
    pieces = loc.split('/')
    while pieces[-1:] == [""]:
        pieces.pop()
    while len(pieces) > 0 and pieces[0] != "cgi-bin":
        pieces.pop(0)
    return "/".join(pieces)

def print_location(req):
    print(f"Location: {crop_location(r.headers['Location'])}")






print("Doing the original POST...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":123, "name":"foobar"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the PUT...")
r = requests.put("http://127.0.0.1/cgi-bin/school/students/123",
                 json = {"name":"changed"},
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of one object) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students/123",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
print(json.dumps(r.json(), sort_keys=True, indent=2))
print()


print("END TESTCASE")

