# numbers = [5, 1, 3, 2, 4]

# print(type(sorted(numbers)))

# print(numbers)

# names = ["Cisco", "Arista", "Juniper"]

# print(sorted(names))

# print(names)

# inventory = [
#     {"hostname": "SW1"},
#     {"hostname": "R1"},
#     {"hostname": "LEAF1"},
# ]


# def view_sorted_devices(inventory):
#     sorted_inventory = sorted(
#         inventory, key=lambda device: device["hostname"], reverse=True
#     )

#     print(sorted_inventory)
#     for index, device in enumerate(sorted_inventory, start=1):
#         print(f"{index}.")
#         print(f"Hostname: {device['hostname']}")
#         print()


# view_sorted_devices(inventory)

inventory = [
    {"hostname": "LEAF2", "vendor": "Cisco"},
    {"hostname": "SPINE1", "vendor": "Arista"},
    {"hostname": "LEAF1", "vendor": "Cisco"},
    {"hostname": "SPINE2", "vendor": "Juniper"},
]


def sort_devices(inventory):

    allowed_fields = [
        "hostname",
        "vendor",
        "role",
    ]
    user_input = input("Sort by (hostname/vendor/role): ")

    if user_input not in allowed_fields:
        print("Invalid field.")
        return

    sorted_inventory = sorted(
        inventory,
        key=lambda device: device[user_input],
    )

    for index, device in enumerate(sorted_inventory, start=1):
        print(f"{index}.")
        print(f"Hostname: {device['hostname']}")
        print(f"Vendor: {device['vendor']}")


sort_devices(inventory)
