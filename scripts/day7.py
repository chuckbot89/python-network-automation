added_devices = []


def add_device(inventory):

    hostname = input("hostname? ")
    ip = input("ip? ")
    role = input("role? ")
    vendor = input("vendor? ")

    device = {"hostname": hostname, "ip": ip, "role": role, "vendor": vendor}

    if not hostname:
        print("Hostname cannot be empty.")
        return
    if not ip:
        print("IP cannot be empty.")
        return
    if not role:
        print("Role cannot be empty.")
        return
    if not vendor:
        print("Vendor cannot be empty.")
        return
    else:
        inventory.append(device)
        print("Device added successfully.")


add_device(added_devices)
print(added_devices)
