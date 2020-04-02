from socket import *
import json

server_port = 53533

serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind(('', server_port))
host_ip_map = {}


def get_response(query_message):
    print('Message:= ', query_message)
    message = json.loads(query_message.decode())
    request_type = message['TYPE']
    hostname = message['NAME']
    ttl = 'TTL' in message

    if not ttl:
        return response_dns_query(request_type, hostname)
    else:
        ip_address = message['VALUE']
        ttl = message['TTL']
        return response_register_query(request_type, hostname, ip_address, ttl)


def response_dns_query(request_type, hostname):
    content = host_ip_map[request_type + ' ' + hostname]
    fs_ip = content['VALUE']
    return str(fs_ip).encode()


def response_register_query(request_type, hostname, ip_address, ttl):
    content = {'TYPE': request_type, 'NAME': hostname, 'VALUE': ip_address, 'TTL': ttl}
    key = request_type + ' ' + hostname
    host_ip_map[key] = content
    return json.dumps(content).encode()


while True:
    query_message, addr = serverSock.recvfrom(2048)
    response_message = get_response(query_message)
    serverSock.sendto(response_message, addr)