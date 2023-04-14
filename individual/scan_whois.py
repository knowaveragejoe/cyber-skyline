import socket

WHOIS_SERVER = "whois.services.cityinthe.cloud"
WHOIS_PORT = 4343
DOMAINS_FILE = "top_10000_domains.txt"

def get_top_domains():
    with open(DOMAINS_FILE, "r") as file:
        domains = [line.strip() for line in file.readlines()]
    return domains

def query_whois_server(domain, server, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server, port))
        sock.sendall(f"{domain}\r\n".encode("utf-8"))

        data = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk

    return data.decode("utf-8")

def main():
    top_domains = get_top_domains()

    for domain in top_domains:
        response = query_whois_server(domain, WHOIS_SERVER, WHOIS_PORT)

        if "flag" in response.lower():
            print(f"Flag found in domain: {domain}")
            print(response)
            break
    else:
        print("Flag not found in the top 1000 domains.")

if __name__ == "__main__":
    main()
