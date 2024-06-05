from ipaddress import *

net = ip_network('135.12.171.214/255.255.248.0', 0) #ip/maska (can be count.(1) )
print(net)
print(net.netmask) #полная запись маски, если та была записана в виде десятичного числа -- количества единиц
print(net.broadcast_address) #широковещательный адрес. узел. не может быть использован для девайсов
print(net.num_addresses) #количество возможных адресов, включая узлы
#все айпишники, не являющимися узлами
ip = ip_address('238.237.149.255')
for mask in range(31):
    net[0] = ip_network(f'ip/{mask}', 0)
    if net[0] < ip < net[-1]: #проверка на то, что айпи не является узлом
        print(mask, net)



print(bin(110)[2:].zfill(8))
bin(255).count("1")


# ip1= [bin(int(x))[2:].zfill(8) for x in '156.133.216.35'.split('.')]





