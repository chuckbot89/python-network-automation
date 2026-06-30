import json

inventory = []


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
    inventory.append(device)
    print("Device added successfully.")


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

    check_device = input("Enter hostname: ")

    for device in inventory:
        if check_device == device["hostname"]:
            inventory.remove(device)
            print("Device deleted successfully.")
            return

    print("Device not found.")


def save_inventory(inventory):
    with open("data/inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully.")


def load_inventory():
    try:
        with open("data/inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    except FileNotFoundError:
        print("Inventory file not found.")
        return []


def search_device(inventory):
    hostname_input = input("Enter hostname: ")

    for device in inventory:
        if hostname_input == device["hostname"]:
            print(f"Hostname: {device['hostname']}")
            print(f"IP: {device['ip']}")
            print(f"Role: {device['role']}")
            print(f"Vendor: {device['vendor']}")
            print()
            return
    print("Device not found.")


def search_by_vendor(inventory):

    found = False

    vendor_input = input("Enter vendor: ").lower()

    for device in inventory:
        if vendor_input == device["vendor"].lower():
            found = True
            print(f"Hostname: {device['hostname']}")
            print(f"IP: {device['ip']}")
            print(f"Role: {device['role']}")
            print(f"Vendor: {device['vendor']}")
            print()

    if not found:
        print("Device not found.")


def search_by_role(inventory):

    found = False

    role_input = input("Enter role: ").lower()

    for device in inventory:
        if role_input == device["role"].lower():
            found = True
            print(f"Hostname: {device['hostname']}")
            print(f"IP: {device['ip']}")
            print(f"Role: {device['role']}")
            print(f"Vendor: {device['vendor']}")
            print()

    if not found:
        print("Device not found.")


inventory = load_inventory()

while True:
    try:
        select_menu = int(
            input(
                """===== Device Inventory =====

1. Add Device
2. View Devices
3. Update Device
4. Delete Device
5. Save Inventory
6. Load Inventory
7. Search Device
8. Search by Vendor
9. Search by Role
10. Exit

Select Menu: """
            )
        )
        if select_menu not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print("Invalid option. Try again!")
        else:
            if select_menu == 1:
                add_device(inventory)
            elif select_menu == 2:
                view_devices(inventory)
            elif select_menu == 3:
                update_device(inventory)
            elif select_menu == 4:
                delete_device(inventory)
            elif select_menu == 5:
                save_inventory(inventory)
            elif select_menu == 6:
                inventory = load_inventory()
            elif select_menu == 7:
                search_device(inventory)
            elif select_menu == 8:
                search_by_vendor(inventory)
            elif select_menu == 9:
                search_by_role(inventory)
            elif select_menu == 10:
                print("Exit")
                break

    except ValueError:
        print("Enter number")
