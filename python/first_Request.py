import requests
url = "https://www.google.com"
response = requests.get(url)
print(f"your request to {url} and the status code is {requests.status_code}")
