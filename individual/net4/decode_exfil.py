import base64
from scapy.all import rdpcap, DNSQR

def decode_base64_subdomain(subdomain):
    try:
        decoded_data = base64.b64decode(subdomain)
        return decoded_data
    except Exception as e:
        print(f"Error decoding base64 subdomain: {e}")
        return None

def parse_packet_capture(file_path):
    packets = rdpcap(file_path)
    extracted_data = []

    for packet in packets:
        if packet.haslayer(DNSQR):
            query = packet[DNSQR].qname.decode("utf-8")
            subdomain = query.split(".")[0]
            decoded_data = decode_base64_subdomain(subdomain)
            if decoded_data:
                extracted_data.append(decoded_data)

    return extracted_data

def main():
    file_path = "ponder.pcapng"
    extracted_data = parse_packet_capture(file_path)

    for i, data in enumerate(extracted_data):
        print(f"Decoded data {i + 1}:")
        print(data)
        print("\n")

if __name__ == "__main__":
    main()
