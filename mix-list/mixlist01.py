#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# solution 1 - concatenating strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# solution 2 - comma seperator
print(f"IP addresses:", iplist[3], ", and", iplist[4])

#solution3 - use an f-string
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
