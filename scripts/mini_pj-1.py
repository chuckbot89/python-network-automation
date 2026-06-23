import json

devices = [
    {"hostname": "LEAF-01", "ip": "10.1.1.1", "status": "up"},
    {"hostname": "LEAF-02", "ip": "10.1.1.2", "status": "down"},
    {"hostname": "SPINE-01", "ip": "10.1.1.254", "status": "up"},
]

devices = []


def show_all_devices():
    all_devices = []
    for device in devices:
        all_devices.append(device["hostname"])
    return all_devices


def search_device():
    device_name = ""
    search = input("Enter Hostname: ").lower()

    for device in devices:
        if search == device["hostname"].lower():
            device_name = device["hostname"]
    return device_name


def show_down_devices():
    down_devices = []
    for device in devices:
        if device["status"] == "down".lower():
            down_devices.append(device["hostname"])
    return down_devices


def show_summary():
    total = len(devices)
    up_device = 0
    down_device = 0

    for device in devices:
        if device["status"] == "up".lower():
            up_device += 1
        else:
            down_device += 1
    return print(
        f"""Total Devices : {total}
Up Devices    : {up_device}
Down Devices  : {down_device}
"""
    )


def save_inventory():
    with open("data/devices.json", "w") as file:
        json.dump(devices, file)
    print("Inventory Saved")


def load_inventory():
    with open("data/devices.json", "r") as file:
        return json.load(file)


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


while True:
    try:
        select_menu = int(
            input(
                """===== Device Inventory =====

1. Add Device
2. Show All Devices
3. Search Device
4. Show Down Devices
5. Show Summary
6. Save Inventory
7. Load Inventory
8. Exit

Select Menu: """
            )
        )
        if select_menu not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("Invald option. Try again!")
        else:
            if select_menu == 1:
                add_device(devices)
            elif select_menu == 2:
                print(search_device())
            elif select_menu == 3:
                print(search_device())
            elif select_menu == 4:
                print(show_down_devices())
            elif select_menu == 5:
                show_summary()
            elif select_menu == 6:
                save_inventory()
            elif select_menu == 7:
                print(load_inventory())
            elif select_menu == 8:
                print("Exit")
                break

    except ValueError:
        print("Enter number")

    except FileNotFoundError:
        print("Check out the Dir")
