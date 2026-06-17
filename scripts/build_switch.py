def build_switch(hostname, ip, model):

    return {
        "hostname": hostname,
        "ip": ip,
        "model": model
    }

switch = build_switch(
    hostname = "N9K-1",
    ip = "10.10.10.1",
    model = "Nexus 93180YC-FX"
)

# print(switch["hostname"])

switch1 = build_switch(
    "LEAF-01",
    "10.1.1.1",
    "N9K"
)

switch2 = build_switch(
    "LEAF-02",
    "10.1.1.2",
    "N9K"
)

switch3 = build_switch(
    "SPINE-01",
    "10.1.1.254",
    "N9K"
)

devices = [
    switch1,
    switch2,
    switch3
]

# print(devices)

for device in devices:
    print(
        f"Connected to {device['hostname']} "
        f"{device['ip']}"
    )
