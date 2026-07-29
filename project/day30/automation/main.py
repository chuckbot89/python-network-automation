from backup.eos import backup as eos_backup
from backup.nxos import backup as nxos_backup

eos_backup("Leaf1")
nxos_backup("Leaf2")
