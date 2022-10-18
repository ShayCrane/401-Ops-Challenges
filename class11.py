#!/usr/bin/python3


# Scrhostt Name: Scapy Pt. 1
# Author: Shay Crane
# Date of last revision: 10/17/2022
# Purpose: create a TCP Port Range Scanner That tests
#  whether a TCP poert is open or closed


# import libraries
from sys import flags
from scapy.all import ICMP, IP, sr1, sr, TCP
import random

# define variables
# can use scanme.nmap.org in place of IP
host=input("Enter an IP or scanme.nmap.org: ")
port_range=[22,23,80,443,3389]

# for loop
# is port_range the last number? if so, break and end scrhost; if not, scan:
for dst_port in port_range:
    src_port=random.randint(1025,65534)
    response=sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0,) # ping and scan
    print(response)

# if / elif / else
# check flag; print to screen
# pseudo code
    if response==None: 
        print(str(host)+":"+str(dst_port)) 
        print("was silently dropped.")
    elif(response.haslayer(TCP)): 
        if(response.getlayer(TCP).flags == 0x12): 
            print(str(host)+":"+str(dst_port))
            print("is open.")
        if(response.getlayer(TCP).flags == 0x14):
            print(str(host)+":"+str(dst_port))
            print("is closed.")
    else: 
        print(host+":"+dst_port)
        print("was silently dropped")



