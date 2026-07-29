# Day20 Assignment - Multiple Objects


class Device:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def show_info(self):
        print(f"{self.hostname}: {self.ip}")

    def change_ip(self, new_ip):
        self.ip = new_ip


# 1.
# 아래 객체를 생성하세요.

leaf1 = Device("Leaf1", "10.1.1.1")
leaf2 = Device("Leaf2", "10.1.1.2")
spine1 = Device("Spine1", "10.1.2.1")


# 2.
# devices 리스트에 세 객체를 저장하세요.

devices = [leaf1, leaf2, spine1]

# 3.
# for문으로 모든 장비의 정보를 출력하세요.

for device in devices:
    device.show_info()

# 4.
# for문으로 모든 장비의 IP를 "192.168.100.1"로 변경하세요.

for device in devices:
    device.change_ip("192.168.100.1")

# 5.
# 다시 모든 장비 정보를 출력하여 변경되었는지 확인하세요.

for deivce in devices:
    device.show_info()

# 6. (생각 문제)
#
# 아래 코드에서
#
# backup = devices
#
# 를 실행한 후
#
# backup[0].change_ip("1.1.1.1")
#
# 를 실행하면
#
# devices[0].ip는 어떻게 될까요?
#
# 이유까지 설명해 보세요.

devices[0].ip 는 1.1.1.1 일꺼야. shallow copy 이기 때문에 backup을 하더라도 devices와 backdup objects가 leaf1,2 and spine1를 똑같이 reference 하고 있어.

# GitHub
#
# Branch
# feature/day20-multiple-objects
#
# Commit
# feat: manage multiple device objects
