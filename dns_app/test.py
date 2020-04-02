import requests
import json

# Testing for registration

fs_url = 'http://172.18.0.3:9090/register'

fibonacci = {
"hostname": "fibonacci.com",
"ip": "172.18.0.3",
"as_ip": "172.18.0.4",
"as_port": "53533"
}

fibo = {
  "hostname": "fibo.com",
  "ip": "172.18.0.3",
  "as_ip": "172.18.0.4",
  "as_port": "53533"
}


response1 = requests.put(fs_url, json=fibonacci)
response2 = requests.put(fs_url, json=fibo)

print(response1)
print(response2)