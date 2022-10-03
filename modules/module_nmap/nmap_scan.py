import nmap
import socket

def getIP(host):
    return socket.gethostbyname(host)

def string_process(host):
    string_replace = ["http://", "https://"]
    for method in string_replace:
        if host.startswith(method):
            host = host.replace(method, "")
            if host.endswith("/"):
                host = host.replace("/", "")
    return host

def nmap_scan():
    print("Infomation Gathering")
    host = input("[+] Enter host to scan <IP or Domain Name>: ")
    if host.startswith("http"):
        host = string_process(host)
        host_IP = getIP(host)
    portScanner = nmap.PortScanner()
    result = portScanner.scan(host_IP, arguments="-T4 -sC -O")
    print(result)
nmap_scan()