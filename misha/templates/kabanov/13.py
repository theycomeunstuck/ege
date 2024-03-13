from ipaddress import *

net = ip_network('135.12.171.214/255.255.248.0', 0) #ip/maska (can be count.(1) )
print(net)
print(net.netmask) #полная запись маски, если та была записана в виде десятичного числа -- количества единиц
print(net.broadcast_address) #широковещательный адрес. узел. не может быть использован для девайсов

#все айпишники, не являющимися узлами Ф
ip = ip_address('238.237.149.255')
for mask in range(31):
    net[0] = ip_network(f'ip/{mask}', 0)
    if net[0] < ip < net[-1]:
        print(mask, net)


