import socket
from urllib.request import urlopen
import re

def get_top_domains():
    # open domains.txt and read into domains
    with open('domains.txt', 'r') as f:
        domains = f.read().splitlines()

    return domains

def query_whois_server(domain, server, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server, port))
        sock.sendall((domain + '\r\n').encode('utf-8'))
        data = sock.recv(1024)
        return data.decode('utf-8')

def find_flag_in_whois(top_domains, server, port):
    for domain in top_domains:
        print(domain)
        whois_data = query_whois_server(domain, server, port)
        if "No Data Found" not in whois_data:
            print ("found something?")
            return True

    return None

if __name__ == '__main__':
    top_domains = get_top_domains()
    print(top_domains)
    whois_server = 'whois.services.cityinthe.cloud'
    whois_port = 4343

    flag = find_flag_in_whois(top_domains, whois_server, whois_port)
    if flag:
        print(f"Flag found: {flag}")
    else:
        print("Flag not found.")