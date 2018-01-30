from collections import Counter
import re


pattern = r"(?<=switchport trunk allowed vlan )[\d,]+"

myLiszt = list()  # List to save data
common_vlans = list()
unique_vlans = list()

number_of_lines = 0


for i, line in enumerate(open('commands.txt')):
    for match in re.finditer(pattern, line, re.MULTILINE):  # Apply the regex in every line
        splitted_line = match.group().split(',')
        n = 0  
        for i in splitted_line:
            if i.isdigit():
                myLiszt.append(splitted_line[n])
            n += 1
        number_of_lines += 1


counter = Counter(myLiszt)
for vlan in counter.iteritems():
    if vlan[1] == number_of_lines:  # VLAN appears in every line = common VLAN
        common_vlans.append(vlan[0])
    if vlan[1] == 1:
        unique_vlans.append(vlan[0])  # IVLAN appears only once = unique VLAN


common_vlans.sort(key=int)  # Sort lists in ascending order
unique_vlans.sort(key=int)

print "List_1 =", common_vlans
print "List_2 =", unique_vlans