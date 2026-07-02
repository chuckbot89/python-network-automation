inventory = [
    {"hostname": "LEAF2", "vendor": "Cisco"},
    {"hostname": "SPINE1", "vendor": "Arista"},
    {"hostname": "LEAF1", "vendor": "Cisco"},
    {"hostname": "SPINE2", "vendor": "Juniper"},
]

# hostnames = []

# for device in inventory:
#     hostnames.append(device["hostname"])

# hostnames = [device["hostname"] for device in inventory]

# print(hostnames)

# vendors = []

# for device in inventory:
#     vendors.append(device["vendor"])

# vendors = [device["vendor"] for device in inventory]

# print(vendors)

# cisco_devices = [device for device in inventory if device["vendor"] == "Cisco"]

# p.pprint(cisco_devices)

vendors = [device["vendor"] for device in inventory]

print(vendors)

vendors = [device["hostname"] for device in inventory]

print(vendors)

vendors = [device["hostname"] for device in inventory if device["vendor"] == "Cisco"]

print(vendors)
