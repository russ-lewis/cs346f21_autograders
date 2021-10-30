#! /usr/bin/python3

import requests
import json

import os
os.system("bash setup_empty_server")



def crop_location(loc):
    pieces = loc.split('/')
    while pieces[-1:] == [""]:
        pieces.pop()
    while len(pieces) > 0 and pieces[0] != "cgi-bin":
        pieces.pop(0)
    return "/".join(pieces)

def print_location(req):
    print(f"Location: {crop_location(r.headers['Location'])}")



def dump_objects(data):
    for obj in data:
        obj["link"] = "...(edited by testcase)... "+crop_location(obj["link"])
    print(json.dumps(sorted(data, key = lambda x: x["id"]),
                     sort_keys=True, indent=2))



print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc110"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc120"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc352"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc210"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"basketweaving101"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/courses",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("END TESTCASE")

