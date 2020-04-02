from flask import Flask
from flask import request
from flask import Response
from socket import *
import requests
import json

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def query_us():
    hostname = request.args.get('hostname', '')
    number = request.args.get('number', '')
    fs_port = request.args.get('fs_port')
    as_ip = request.args.get('as_ip')
    as_port = int(request.args.get('as_port'))
    if hostname == '' or number == '' or fs_port == '' or as_ip == '' or as_port == '':
        return Response("Bad Request", status=400)
    fs_ip = query_as(as_ip, as_port, hostname)
    fs_url = "http://" + fs_ip + ":" + fs_port + "/fibonacci?number=" + number
    print(fs_url)
    res = requests.get(fs_url)
    if res.status_code == 400:
        return " Bad format"
    return res.text


def query_as(as_ip, as_port, hostname):
    client_socket = socket(AF_INET, SOCK_DGRAM)
    query_json = {'TYPE': 'A', 'NAME': hostname}
    client_socket.sendto(json.dumps(query_json).encode(), (as_ip, as_port))
    ip_address, server_address = client_socket.recvfrom(2048)
    return ip_address.decode()



app.run(host='0.0.0.0',
        port=8080,
        debug=False)