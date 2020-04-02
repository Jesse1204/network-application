import socket
import json

UDP_PORT_NO = 53533

# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(('', UDP_PORT_NO))
map = {}

def buildResponse(request):
    print('Received request:= ', request)
    json_obj = json.loads(request.decode().replace("\'", "\""))
    type = json_obj['TYPE']
    hostname = json_obj['NAME']
    is_register_request = 'VALUE' in json_obj

    if not is_register_request:
        return build_get_dns_response(type, hostname)
    else:
        ip_address = json_obj['VALUE']
        ttl = json_obj['TTL']
        return build_register_response(type, hostname, ip_address, ttl)


def build_get_dns_response(type, hostname):
    json_string = map[type + ' ' + hostname]
    return str(json_string).encode()


def build_register_response(type, hostname, ip_address, ttl):
    json_string = {'TYPE': type, 'NAME': hostname, 'VALUE': ip_address, 'TTL': ttl}
    key = type + ' ' + hostname
    map[key] = json_string
    return str(json_string).encode()


while True:
    request, addr = serverSock.recvfrom(2048)
    response = buildResponse(request)
    serverSock.sendto(response, addr)