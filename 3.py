import re

pattern = r"(?P<input>\w+)\s*(?P<prefix>\d*\.\d*\.\d*\.\d*)\s*\[(?P<metric>\d*\/\d*)\]\s*via" \
          r"\s*(?P<via>\d*\.\d*\.\d*\.\d*)\s*,\s*(?P<time>\d*.\d*.\d*)\s*,\s*(?P<interface>.*)"

dic={'L' : 'local', 'C' : 'connected', 'S' : 'static', 'R' : 'RIP', 'M' : 'mobile', 'B' : 'BGP',
       'D' : 'EIGRP', 'EX' : 'EIGRP external', 'O' : 'OSPF', 'IA' : 'OSPF inter area',
       'N1' : 'OSPF NSSA external type 1', 'N2' : 'OSPF NSSA external type 2',
       'E1' : 'OSPF external type 1', 'E2' : 'OSPF external type 2', 'E' : 'EGP',
       'i' : 'IS-IS', 'su' : 'IS-IS summary', 'L1' : 'IS-IS level-1', 'L2' : 'IS-IS level-2',
       'ia' : 'IS-IS inter area', '*' : 'candidate default', 'U' : 'per-user static route',
       'o' : 'ODR', 'P' : 'periodic downloaded static route', 'H' : 'NHRP', 'l' : 'LISP',
       'a' : 'application route',
       '+' : 'replicated route', '%' : 'next hop override'}

protocols = list()
prefix = list()
ad = list()
nexthop = list()
last_update = list()
ifout = list()


for i, line in enumerate(open('ShowIpRoute.txt')):
    for match in re.finditer(pattern, line, re.MULTILINE):  # Apply the regex in every line
        protocols.insert(i,dic[match.group('input')])
        prefix.insert(i, match.group('prefix'))
        ad.insert(i, match.group('metric'))
        nexthop.insert(i, match.group('via'))
        last_update.insert(i, match.group('time'))
        ifout.insert(i, match.group('interface'))


for j in range(0, len(protocols)):  # Every list has the same length
    print "Protocol:           " + protocols[j]
    print "Prefix:             " + prefix[j]
    print "AD/Metric:          " + ad[j]
    print "Next-Hop:           " + nexthop[j]
    print "Last Update:        " + last_update[j]
    print "Outbound interface: " + ifout[j]+"\n"