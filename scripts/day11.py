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
    {"hostname": "R1", "ip": "10.1.1.1"},
    {"hostname": "SW1", "ip": "10.1.1.2"},
    {"hostname": "LEAF1", "ip": "10.1.1.3"},
]

# device_map = {device["hostname"]: device["ip"] for device in inventory}

# print(device_map)

# device_map = {device["hostname"]: device for device in inventory}

# print(device_map)
# requried_fields = ["R1", "SW1", "LEAF1"]


def search_device():

    user_input = input("Type in a hostname: ")

    device_map = {device["hostname"]: device for device in inventory}

    if user_input not in device_map:
        print("Invalid")
        return

    device = device_map[user_input]
    print(device)


search_device()
