# knock_test

This is a simple script to test knock port sequences. 
This is run like this: python3.9 knock_test.py 

Variables to edit

dstIP = "192.168.0.10"  # [EDIT] change this to target IP

tport = 22              # [EDIT] test port 22 (SSH)

port_list = [10001,10011,10111] # [EDIT] change this to the list of possible port numbers


If there are more/less than 3 ports you need to add {} and i[#] to the line

os.system('knock {} {} {} {} -d 500'.format(dstIP, i[0], i[1], i[2])) # [EDIT] add/remove values depending on the number of ports
