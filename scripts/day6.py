import json

devices = [{"hostname": "LEAF-01", "ip": "10.1.1.1", "status": "up"}]

with open("data/devices.json", "w") as file:
    json.dump(devices, file)

with open("data/devices.json", "r") as file:
    data = json.load(file)

print(data[0]["hostname"])
