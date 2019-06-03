#!/usr/bin/python2

import socket

host = "ip_address"
port = insert_port

headers = """\
POST /path HTTP/1.1\r
Host: {host}\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate\r
Referer: http://{host}/path\r
Connection: keep-alive\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
\r\n"""

body_bytes = "request data\r\n"

header_bytes = headers.format(
    content_type="text/plain",
    content_length=len(body_bytes),
    host=str(host) + ":" + str(port)
).encode('iso-8859-1')

payload = header_bytes + body_bytes

print "SENDING PAYLOAD..."
print payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(payload)
