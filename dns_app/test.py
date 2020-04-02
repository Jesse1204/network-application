import requests
import json

url = 'http://172.18.0.3:9090/register'

eg = {
"hostname": "fibonacci.com",
"ip": "172.18.0.3",
"as_ip": "172.18.0.4",
"as_port": "53533"
}

x = {
  "hostname": "fibo.com",
  "ip": "172.18.0.3",
  "as_ip": "172.18.0.4",
  "as_port": "53533"
}

json_obj = json.dumps(x)


headers = {"Content-Type": "application/json"}

response1 = requests.put(url, json=x)
response2 = requests.put(url, json=eg)

print(response1)
print(response2)