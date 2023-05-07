import requests

url = "https://httpbin.org/post"
head = {"Content-Type": "application/json"}
data = {"name":"Bogdan"}


def post():
    return requests.post(url, json=data, headers = head).json()

if __name__ == "__main__":
    print(post())
