# DoSer

Implementation of different DoS techniques

The project is under development

Note: Not all of the attacks are guaranteed to work, especially to systems that has vulnerabilities fixed and protection setted up. Please be understood each DoS attack before using them, since the project is only for educational purpose only.

## What is it

Denial of Service (DoS) is an attack on the Internet that is intended to disable the proper usage of a service.

Examples:
- A hacker kicks an internet user out of his wireless connection 
- Massive amount of data transmission causing stress on online systems
- Exploit a certain vulnerability to cause system crash
...


## Types of DoS attacks:
- Deauthentication
- SYN flooding
- UDP flooding
- ICMP flooding
- Ping of death
- Smurf attack
- Man in the middle
- IP fragmentation (Teardrop attack)

### Deauthentication
It is a type of attack such that a hacker forces deconnection of an internet user out of his network. This type of attack does not require internet connection and encryption.

#### Methodology:
- The hacker sends deauthentication frame to the gateway with the spoofed MAC address of the victim. 
- The gateway believes that the victim requests deauthentication, and closes the connection.

### SYN flooding
It is a type of attack such that a hacker creates massive amount of TCP SYN packet, forcing the victim service to reply SYN/ACK for each SYN packet sent and wait for the ACK responce, which would never be sent. The attack forces the victim service to open massive amount of sessions which ultimately exhaust its resource.

The connection timeout for TCP is 75 seconds, thus the greatest effect of DoS would be achieved with 75 seconds of attack.

### UDP flooding
It is a type of attack such that a hacker creates massive amount of UDP packet, causing the victim service to consistently check non-existent services in a high rate.

### ICMP flooding
It is a type of attack such that a hacker creates massive amount of ICMP packet, forcing the victim's system to reply and exhaust the victim's network bandwidth.

### Ping of death
This attack tries to crash a system by feeding it an oversized ICMP packet such as a size of 65538 bytes. (The maximim size of an ICMP packet data is 65535 bytes)

### Smurf attack
The attacker spoofs the victim's IP address, sending massive amount of ICMP broadcast packet to the network. This causes all systems in the network to respond the ICMP packet and send all their replies to the victim's system.

### Man in the middle
The attacker uses ARP spoofing to sit in the middle of the victim's connection, but does not forward the Internet.

### IP fragmentation attack (Teardrop attack)
The attacker sends fragmented packets to the victim, and using a bug in the IP reassembly, the attacker prevents the victum from reassemble the fragments and causes them to overlap. This could result the victim system to crash.