#! /usr/bin/python3

import requests

import os
os.system("bash setup_empty_server")


print("Building a small student/course database...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":123, "name":"foobar"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc110"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/students/123/courses",
                  json = "csc110",
                  allow_redirects = False)
print()


print("This should be 409, once")
r = requests.delete("http://127.0.0.1/cgi-bin/school/courses/csc110")
print(f"Status: {r.status_code}")
print()


print("END TESTCASE")

