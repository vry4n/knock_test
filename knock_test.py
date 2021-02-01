#!/usr/bin/python3
# Release: 1.0
# Author: Bryan Alfaro (Vry4n)
# This is intended to test port knocking combination of ports when we have the list but not the sequence
# Run: python3.9 knock_test.py
# Change the values labled as [EDIT]
# Source: https://vk9-sec.com

from itertools import permutations
from time import sleep
import os
import re

dstIP = "192.168.0.10"  # [EDIT] change this to target IP
tport = 22              # [EDIT] test port 22 (SSH)
port_list = [10001,10011,10111] # [EDIT] change this to the list of possible port numbers

# This for loop will iterate through port_list values and generate different combinations
# It will then test each combination using knock command. Disclaimer: you need that installed as well as nmap
# THe script will then scan the port for the status using nmap
count = 0
for i in permutations(port_list):
    count += 1
    print('Test {}: {}'.format(count, i))
    print('Running knock')
    print('=' * 80)
    os.system('knock {} {} {} {} -d 500'.format(dstIP, i[0], i[1], i[2])) # [EDIT] add/remove values depending on the number of ports
    sleep(10) # [EDIT] Change this value, it depends on timeout settings in knockd.conf file at the remote server, 10 seconds worked for me, it the time out was 20
    print('Running nmap')
    os.system('nmap -p {} {}'.format(tport, dstIP))
    print('=' * 80)
    sleep(10)
