devices = [
    {"hostname": "LEAF-01", "ip": "10.1.1.1", "status": "up"},
    {"hostname": "LEAF-02", "ip": "10.1.1.2", "status": "down"},
    {"hostname": "SPINE-01", "ip": "10.1.1.254", "status": "up"},
]


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
    down_deivce = 0

    for device in devices:
        if device["status"] == "up".lower():
            up_device += 1
        else:
            down_deivce += 1
    return print(
        f"""Total Devices : {total}
Up Devices    : {up_device}
Down Devices  : {down_deivce}
"""
    )


while True:
    try:
        select_menu = int(
            input(
                """===== Device Inventory =====

        1. Show All Devices
        2. Search Device
        3. Show Down Devices
        4. Show Summary
        5. Exit

        Select Menu: """
            )
        )
        if select_menu not in [1, 2, 3, 4, 5]:
            print("Invald option. Try again!")
        else:
            break
    except ValueError:
        print("Enter number")

if select_menu == 1:
    print(show_all_devices())
if select_menu == 2:
    print(search_device())
if select_menu == 3:
    print(show_down_devices())
if select_menu == 4:
    print(show_summary())
    print("Exit")
