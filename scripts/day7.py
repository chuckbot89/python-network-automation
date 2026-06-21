devices = []


# def add_device(inventory):

#     hostname = input("hostname? ")
#     ip = input("ip? ")
#     role = input("role? ")
#     vendor = input("vendor? ")

#     device = {"hostname": hostname, "ip": ip, "role": role, "vendor": vendor}

#     if not hostname:
#         print("Hostname cannot be empty.")
#         return
#     if not ip:
#         print("IP cannot be empty.")
#         return
#     if not role:
#         print("Role cannot be empty.")
#         return
#     if not vendor:
#         print("Vendor cannot be empty.")
#         return
#     inventory.append(device)
#     print("Device added successfully.")


# add_device(added_devices)
# print(added_devices)


inventory = [
    {"hostname": "R1", "ip": "10.1.1.1", "role": "Core", "vendor": "Cisco"},
    {"hostname": "SW1", "ip": "10.1.1.2", "role": "Access", "vendor": "Cisco"},
]


def view_devices(inventory):

    if not inventory:
        print("No devices found")
        return

    for device in inventory:
        print(f"""Hostname: {device["hostname"]}
IP: {device["ip"]}
Role: {device["role"]}
Vendor: {device["vendor"]}
""")


def update_device(inventory):
    found = False
    check_device = input("Enter hostname: ")

    for device in inventory:
        if check_device == device["hostname"]:
            found = True
            update_ip = input("Enter new IP: ")
            device["ip"] = update_ip
            break

    if not found:
        print("Device not found.")
        return

    print("Device updated successfully.")


def delete_device(inventory):
    found = False
    check_device = input("Enter hostname: ")
    for device in inventory:
        if check_device == device["hostname"]:
            found = True
            inventory.remove(device)
            break

    if not found:
        print("Device not found.")
        return

    print("Device deleted successfully.")


print(delete_device(inventory))
print(inventory)
