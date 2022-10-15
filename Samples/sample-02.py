from ipaddress import ip_address
import socket

in_addr = socket.gethostbyname(socket.gethostname())
# gethostbyname: IP할당/ gethostname: 호스트네임가져오기

print(in_addr)

