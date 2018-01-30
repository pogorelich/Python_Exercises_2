access_template = ["switchport mode access", "switchport access vlan {}","switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"]

trunk_template = ["switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"]


# Get input

ifmode = raw_input("Enter interface mode (access/trunk): ")

iftype = raw_input("Enter interface type and number: ")


# Operate with received input

if ifmode == "access" or ifmode == "Access" or ifmode == "ACCESS":
    
    vlan = raw_input("Enter VLAN number: ")
    
    print "Interface", iftype
    print access_template[0]
    print access_template[1].replace("{}",vlan)
    print access_template[2]
    print access_template[3]
    print access_template[4]

elif ifmod == "trunk" or ifmode == "Trunk" or ifmode == "TRUNK":
    
    vlans = raw_input("Enter allowed VLANs: ")
    
    print "Interface", iftype
    print trunk_template[0]
    print trunk_template[1]
    print trunk_template[2].replace("{}", vlans)

else:

    print "Interface mode not supported"