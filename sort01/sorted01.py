#!/usr/bin/env python3

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']
print("Currently the value of vendor:", vendors)
print("\nThe results of sorted() function:", sorted(vendors))
print("But the value of the list hasn't actually changed:", vendors)

sortedvendors = sorted(vendors)
print('\nOur sorted vendor list looks like this: ' + str(sortedvendors))
baksortvendors = sorted(vendors, reverse=True)
print('Our reverse sorted vendor list looks like this: ', baksortvendors)

vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', \
'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']
print('\nOur new vendordeux list looks like this: ', vendorsdeux)
print('Our sorted vendor list looks like this: ', sorted(vendorsdeux))
