#! /usr/bin/python3


import requests


print("This should be error 400, four times")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":"asdf"})
print(f"Status: {r.status_code}")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"name":"Russell Lewis"})
print(f"Status: {r.status_code}")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"russ":"trying hard to come up with good testcases"})
print(f"Status: {r.status_code}")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":"not_an_integer", "name":"Russ"})
print(f"Status: {r.status_code}")
print()


print("Building a small student/course database, but with no registrations...")
r = requests.post("http://127.0.0.1/cgi-bin/school/students",
                  json = {"id":123, "name":"foobar"},
                  allow_redirects = False)
r = requests.post("http://127.0.0.1/cgi-bin/school/courses",
                  json = {"id":"csc110"},
                  allow_redirects = False)
print()


print("This should be 400, once")
r = requests.post("http://127.0.0.1/cgi-bin/school/students/123/courses", json="csc210")
print(f"Status: {r.status_code}")
print()


print("END TESTCASE")

