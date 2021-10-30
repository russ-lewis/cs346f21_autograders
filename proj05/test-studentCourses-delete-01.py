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



print("POST-ing several students...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":123, "name":"foobar"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":456, "name":"Albrert Einstein"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":2, "name":"Steve Wozniak"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":17, "name":"Lt. Cmdr. Data"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":1024, "name":"Commander Tucker"},
                  allow_redirects = False)
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)

print("POST-ing several courses...")
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc110"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc120"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc352"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc210"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"basketweaving101"},
                  allow_redirects = False)


print("Doing the GET (of the whole student collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
dump_objects(r.json())
print()

print("Doing the GET (of the whole course collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/courses",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
dump_objects(r.json())
print()


print("Doing several student course POSTs...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students/123/courses",
                  json = "csc110",
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students/123/courses",
                  json = "csc120",
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students/123/courses",
                  json = "csc352",
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students/456/courses",
                  json = "csc120",
                  allow_redirects = False)


print("Doing the GET (of the whole student collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
dump_objects(r.json())
print()

print("Doing the GET (of the whole course collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/courses",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
dump_objects(r.json())
print()


print("Deleting one student...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/123",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Deleting one student...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/1024",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Deleting one student...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/456",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole student collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
dump_objects(r.json())
print()

print("Doing the GET (of the whole course collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/courses",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print("Body (interpreted from JSON):")
dump_objects(r.json())
print()


print("END TESTCASE")

