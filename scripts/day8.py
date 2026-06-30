inventory = [
    {"hostname": "R1", "ip": "10.1.1.1", "role": "Core", "vendor": "Cisco"},
    {"hostname": "SW1", "ip": "10.1.1.2", "role": "Access", "vendor": "Cisco"},
    {"hostname": "host1", "ip": "1.1.1.1", "role": "access", "vendor": "FortiNet"},
]


def show_total_devices(inventory):
    total_devices = len(inventory)
    print(f"Total Devices: {total_devices}")


def view_devices(inventory):

    if not inventory:
        print("No devices found")
        return

    for index, device in enumerate(inventory, start=1):
        print(f"{index}.")
        print(f"Hostname: {device['hostname']}")
        print(f"IP: {device['ip']}")
        print(f"Role: {device['role']}")
        print(f"Vendor: {device['vendor']}")


show_total_devices(inventory)
view_devices(inventory)
