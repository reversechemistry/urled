import requests

req = requests.get("https://www.tutorialspoint.com/unix/images/unix-mini-logo.jpg")

print(req.raw)