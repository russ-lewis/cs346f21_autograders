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



def dump_objects(data):
    for obj in data:
        obj["link"] = "...(edited by testcase)... "+crop_location(obj["link"])
    print(json.dumps(sorted(data, key = lambda x: x["id"]),
                     sort_keys=True, indent=2))



print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":123, "name":"foobar"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":456, "name":"Albrert Einstein"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":2, "name":"Steve Wozniak"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":17, "name":"Lt. Cmdr. Data"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("Doing the DELETE of 456...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/456",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("POST-ing...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":1024, "name":"Commander Tucker"},
                  allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("Doing the DELETE of 2...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/2",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("Doing the DELETE of 123...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/123",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("Doing the DELETE of 17...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/17",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("Doing the DELETE of 1024...")
r = requests.delete("http://127.0.0.1/cgi-bin/school/students/1024",
                    allow_redirects = False)
print(f"Status: {r.status_code}")
print_location(r)
print()


print("Doing the GET (of the whole collection) afterwards...")
r = requests.get("http://127.0.0.1/cgi-bin/school/students",
                 allow_redirects = False)
print(f"Status: {r.status_code}")
print(f"Body:")
dump_objects(r.json())
print()


print("END TESTCASE")

