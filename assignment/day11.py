# inventory = [
#     {
#         "hostname": "R1",
#         "ip": "10.1.1.1",
#         "vendor": "Cisco",
#     },
#     {
#         "hostname": "SW1",
#         "ip": "10.1.1.2",
#         "vendor": "Cisco",
#     },
# ]

# device_map = {}

# inventory를 순회하면서

# hostname을 Key로

# ip를 Value로

# Dictionary를 만들어라.

# for device in inventory:
#     device_map[device["hostname"]] = device["ip"]


# print(device_map)

# device_map = {device["hostname"]: device["ip"] for device in inventory}

# print(device_map)

inventory = [
    {"hostname": "R1", "ip": "10.1.1.1", "role": "Core", "vendor": "Cisco"},
    {"hostname": "SW1", "ip": "10.1.1.2", "role": "Access", "vendor": "Cisco"},
    {"hostname": "host1", "ip": "1.1.1.1", "role": "access", "vendor": "Juniper"},
    {"hostname": "host1", "ip": "1.1.1.1", "role": "access", "vendor": "FortiNet"},
]


# device_map = {device["hostname"]: device["ip"] for device in inventory}

# print(device_map)

# device_map = {device["hostname"]: device for device in inventory}

# print(device_map)
# requried_fields = ["R1", "SW1", "LEAF1"]


def print_device(device):
    print(f"Hostname: {device['hostname']}")
    print(f"IP: {device['ip']}")
    print(f"Role: {device['role']}")
    print(f"Vendor: {device['vendor']}")


# def search_device():

#     user_input = input("Type in a hostname: ")

#     device_map = {device["hostname"]: device for device in inventory}

#     if user_input not in device_map:
#         print("Invalid")
#         return

#     device = device_map[user_input]

#     print_device(device)


# search_device()


# def search_by_vendor(inventory):

#     for device in inventory:
#         for device_name in device.items():
#             print(device_name)


# search_by_vendor(inventory)

# print(inventory)

vendor_map = {"Cisco": [], "Juniper": []}

for device in inventory:
    vendor = device["vendor"]

    if vendor not in vendor_map:
        vendor_map[vendor] = []

    vendor_map[vendor].append(device)

print(vendor_map)
