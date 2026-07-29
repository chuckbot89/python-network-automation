def build_switch(hostname, ip, status):
    return {"hostname": hostname, "ip": ip, "status": status}


hostname = input("Enter hostname: ")
ip = input("Enter ip: ")
status = ""
while status not in ["up", "down"]:
    status = input("Enter status: ").lower()
    if status not in ["up", "down"]:
        print("Invalid status. Try again.")

print("Device added")

device = build_switch(hostname, ip, status)

print(device)
