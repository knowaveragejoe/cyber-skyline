import base64
from scapy.all import rdpcap, DNSQR, UDP, DNS

def decode_base64_subdomain(subdomain):
    try:
        decoded_data = base64.b64decode(subdomain)
        return decoded_data
    except Exception as e:
        print(f"Error decoding base64 subdomain: {e}")
        return None

def parse_packet_capture(file_path):
    packets = rdpcap(file_path)
    dns_packets = []

    for packet in packets:
        if packet.haslayer(DNSQR) and packet.haslayer(UDP) and packet.haslayer(DNS):
            dns_packets.append(packet)

    sorted_dns_packets = sorted(dns_packets, key=lambda p: (p[UDP].sport, p[DNS].id))

    extracted_data = []

    for packet in sorted_dns_packets:
        query = packet[DNSQR].qname.decode("utf-8")
        subdomain = query.split(".")[0]
        decoded_data = decode_base64_subdomain(subdomain)
        if decoded_data:
            extracted_data.append(decoded_data)

    return extracted_data

def reconstruct_file(extracted_data, output_file):
    with open(output_file, 'wb') as f:
        for data in extracted_data:
            f.write(data)

def main():
    pcap_file_path = "ponder.pcapng"
    output_file = "reconstructed_file.bin"

    extracted_data = parse_packet_capture(pcap_file_path)
    reconstruct_file(extracted_data, output_file)

    print(f"Reconstructed file saved as: {output_file}")

if __name__ == "__main__":
    main()
