from urllib import response
import requests

resp = requests.get("http://127.0.0.1:8000/home-cbv/")
print(resp.content)

resp = requests.post("http://127.0.0.1:8000/home-cbv/", data={"key":"value"})
print(resp.content)

resp = requests.delete("http://127.0.0.1:8000/home-cbv/",)
print(resp.content)

resp = requests.put("http://127.0.0.1:8000/home-cbv/",)
print(resp.content)

resp = requests.patch("http://127.0.0.1:8000/home-cbv/",)
print(resp.content)
