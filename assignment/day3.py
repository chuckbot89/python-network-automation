def build_switch(hostname, ip, status):
    return {
        "hostname": hostname,
        "ip": ip,
        "status": status
    }

# switch1 = build_switch(
#     hostname = "LEAF-01",
#     ip = "10.1.1.1",
#     status = "up"
# )

# switch2 = build_switch(
#     hostname = "LEAF-02",
#     ip = "10.1.1.2",
#     status = "down"
# )

# switch3 = build_switch(
#     hostname = "SPINE-01",
#     ip = "10.1.1.254",
#     status = "up"
# )

# devices = [
#     switch1,
#     switch2,
#     switch3
# ]

# for device in devices:
#     status = device["status"]

#     if status == "up":
#         print("OK")
#     else:
#         print("DOWN")

# for device in devices:
#     hostname = device["hostname"]
#     ip = device["ip"]
#     status = device["status"]

#     print(f'''Hostname: {hostname}
#     IP: {ip}
#     Status: {status}
#     ''')

device = build_switch(
    hostname = input("Enter a hostname: "),
    ip = input("Enter a ip: "),
    status = input("Enter status: ")
)

if device["status"] != "up" or "down":
    print("Invalid Status")
