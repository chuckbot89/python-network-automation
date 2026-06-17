devices = [
    {"hostname": "LEAF-01", "ip": "10.1.1.1", "status": "up"},
    {"hostname": "LEAF-02", "ip": "10.1.1.2", "status": "down"},
    {"hostname": "SPINE-01", "ip": "10.1.1.254", "status": "up"},
]

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
        if select_menu < 1 or select_menu > 5:
            print("Invald option. Try again!")
        else:
            break
    except ValueError:
        print("Enter number")

if select_menu == 1:
    print("Host Name:")
    for device in devices:
        print(device["hostname"])
elif select_menu == 3:
    pass
elif select_menu == 4:
    pass
elif select_menu == 5:
    print("Exit")
