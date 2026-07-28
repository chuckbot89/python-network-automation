from backup import backup
from devices import devices

for device in devices:
    backup(device)
