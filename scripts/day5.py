# while True:
#     try:
#         vlan_id = int(input("Enter VLAN ID: "))

#         if 1 <= vlan_id <= 4094:
#             print("VLAN Accepted")
#             break
#         else:
#             print("Invalid VLAN Range")

#     except ValueError:
#         print("Not INT")

healthy = []
failed = []

# devices = [
#     {"hostname": "LEAF-01", "status": "up"},
#     {"hostname": "LEAF-02", "status": "down"},
#     {"hostname": "SPINE-01", "status": "up"},
#     {"hostname": "SPINE-02", "status": "down"},
# ]

# for device in devices:
#     if device["status"] == "up":
#         healthy.append(device["hostname"])
#     elif device["status"] == "down":
#         failed.append(device["hostname"])

# print("Healthy Devices:")
# for device in healthy:
#     print(device)
# print()
# print("Failed Devices:")
# for device in failed:
#     print(device)

up_count = 0
down_count = 0

# for device in devices:
#     if device["status"] == "down":
#         failed.append(device["hostname"])
#         down_count += 1
#     else:
#         up_count += 1

#     total = down_count + up_count

# print(f"Total Devices : {total}")
# print(f"Up Devices    : {up_count}")
# print(f"Down Devices  : {down_count}")

devices = [
    {"hostname": "LEAF-01", "ip": "10.1.1.1"},
    {"hostname": "LEAF-02", "ip": "10.1.1.2"},
    {"hostname": "SPINE-01", "ip": "10.1.1.254"},
]

found = False
cnt = 0

search = input("Enter Hostname: ")

for device in devices:
    # if search == device["hostname"]:
    if search in device["hostname"]:
        found = True
        cnt += 1
        print(f"Hostname: {device['hostname']}")

if not found:
    print("No Match")

print(f"Matches Found: {cnt}")
