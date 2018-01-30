# Need netaddr to be installed

from netaddr import *
import pprint


# Auxiliary function to verify if an IP address is correct

def correct_ip(ip):
    foo = ip.split('.')
    if len(foo) != 4:
        return 0
    for i in foo:
        if not i.isdigit():
            return 0
        j = int(i)
        if j < 0 or j > 255:
            return 0
    return 1


# Auxiliary function to verify if an IP mask is correct

def correct_mask(mask):
    foo = mask.split('/')
    if len(foo) != 2:
        return 0
    if not foo[1].isdigit():
        return 0
    j = int(foo[1])
    if j < 0 or j > 32:
        return 0
    return 1


# Request input

ip_address = raw_input("Enter Ip address: ")

ip_mask = raw_input("Enter subnet mask in decimal format: ")


# Request input until it is correct

while correct_ip(ip_address) == 0:
    print ("Invalid IP address format")
    ip_address = raw_input("Enter Ip address: ")

while correct_mask(ip_mask) == 0:
    print ("Subnet mask is invalid")
    ip_mask = raw_input("Enter subnet mask in decimal format: ")


# Use netaddr to get broadcast, network and IP addresses

ip_address_bits = IPAddress(ip_address)
ip_with_mask = IPNetwork(ip_address+ip_mask)
ip_network = ip_with_mask.network
ip_broadcast = ip_with_mask.broadcast
splitted_ip = str(ip_address).split('.')


print ("     " + splitted_ip[0] + "       " + splitted_ip[1] + "       " + splitted_ip [2] + "       " + splitted_ip[3])
print ip_address_bits.bits()
print ("network address is: "+str(ip_network))
print ("broadcast address is: "+str(ip_broadcast))