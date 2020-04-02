from flask import Flask
from flask import request
from flask import Response
import json
from socket import *

app = Flask(__name__)


@app.route('/fibonacci', methods=['GET'])
def return_fib():
    number = request.args.get('number')
    print(number)
    print(isinstance(number, str) )
    if number.isdigit():
        int_number = int(number)
        return cal_fib(int_number)
    else:
        return "Bad Format",400


def cal_fib(number):
    if number <= 1:
        return str(number)
    if number == 2:
        return "1"
    cur_num = 0
    prev1 = 1
    prev2 = 1
    for i in range(3, number + 1):
        cur_num = prev1 + prev2
        prev2 = prev1
        prev1 = cur_num
    return str(cur_num)


@app.route('/register', methods=['PUT'])
def register():
    print(request.is_json)
    print (request)
    data = request.get_json()
    hostname = data['hostname']
    fs_ip = data['ip']
    as_ip = data['as_ip']
    as_port = int(data['as_port'])
    register_json = {'TYPE': 'A', 'NAME': hostname, 'VALUE': fs_ip, 'TTL': 10}
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.sendto(json.dumps(register_json).encode(), (as_ip, as_port))
    response_message, server_address = client_socket.recvfrom(2048)
    return response_message.decode(), 201


app.run(host='0.0.0.0',
        port=9090,
        debug=False)
