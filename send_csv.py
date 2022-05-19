import requests

url = "https://httpbin.org/post"
file = {'file': open("/home/pi/testing.csv", "rb")}
r = requests.post(url, files=file)

print(r.status_code)
print(r.text)
