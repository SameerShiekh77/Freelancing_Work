# Part 2
import requests
url = "http://samtech-edu.web.app"
r = requests.get(url)
# print(r.headers)
print(r.url)