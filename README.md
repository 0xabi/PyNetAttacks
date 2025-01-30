# PyNetAttacks
This repository contains Python scripts to simulate various attacks studied during the Computer Security and Wireless Internet courses.

Detailed experiments here: [0xabi Gitbook - PyNetAttacks](https://0xabi.gitbook.io/notes/projects/pynetattacks)

**Network Protocols Attacks**: ICMP Smurf Attack, ICMP Redirect Attack, ARP Cache Poisoning, TCP SYN Flood Attack, TCP RST Attack, TCP Session Hijacking, DNS Local Poisoning, DNS Cache Poisoning, DNS Rebinding Attack, BGP Prefix Attack.

**IEEE 802.11 Attacks**: Deauth. Attack, Autoimmune disorder, Power Save Attack, Virtual Carrier Sensing Attack, BlockACK, Channel Switch Attack, ATIM Attack.

## TCP SYN Flood Attack
To perform a SYN Flood attack, we have to send a lot of SYN messages but without answer back with an ACK message after receiving the SYN-ACK message from the server, in this way we will fill the half-open connection queue.

To notice the attack's effect, we have to consider disabling the SYN cookie mitigation and to choose the correct parameters.

**Disable SYN Cookie**
``` bash
sudo sysctl -w net.ipv4.tcp_syncookies=0
```

**Increase number of SYN-ACK's message retries**
``` bash
sudo sysctl -w net.ipv4.tcp_synack_retries=20
```

**Decrease backlog size**
``` bash
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=80
```

**Flush TCP Cache**
``` bash
sudo ip tcp_metrics flush
```

### Run the attack

**Run the server**
``` bash
sudo python ListenTCP.py
```

**SYN Attack**
``` bash
sudo python SYNFloodScript.py
```

For the full experiment: [0xabi Gitbook - PyNetAttacks - SYN Flood Attack](https://0xabi.gitbook.io/notes/projects/pynetattacks/syn-flood-attack)




