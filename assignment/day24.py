# Day24 Assignment - Polymorphism


class Device:
    def __init__(self, hostname):
        self.hostname = hostname

    def connect(self):
        print(f"{self.hostname} Generic Connection")


# 1.
# CiscoDevice를 만드세요.
# Device를 상속받으세요.
# connect()를 오버라이딩하여
# "{hostname} Cisco NX-OS Connected"
# 를 출력하세요.


class CiscoDevice(Device):
    def connect(self):
        print(f"{self.hostname} Cisco NX-OS Connected")


# 2.
# AristaDevice를 만드세요.
# Device를 상속받으세요.
# connect()를 오버라이딩하여
# "{hostname} Arista EOS Connected"
# 를 출력하세요.


class AristaDevice(Device):
    def connect(self):
        print(f"{self.hostname} Arista EOS Connected")


# 3.
# 객체를 생성하세요.

leaf1 = CiscoDevice("Leaf1")
spine1 = AristaDevice("Spine1")


# 4.
# 리스트에 두 객체를 저장하세요.

devices = [leaf1, spine1]


# 5.
# 반복문을 사용하여
# connect()를 호출하세요.

for device in devices:
    device.connect()

# 6. (생각 문제)

# 왜 아래 코드에는
# if isinstance(...)
# 가 필요 없을까요?

# for device in devices:
#     device.connect()

# 자신의 생각을 주석으로 작성하세요.

"""
device는 반복마다 새로운 객체를 만드는 것이 아니라
리스트에 저장된 객체의 참조를 하나씩 가져온다.

Python은 device가 실제로 어떤 객체인지 확인하고,
그 객체에 맞는 connect() 메서드를 자동으로 호출하므로
if isinstance()가 필요 없다.
"""

# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day24-polymorphism
#
# Commit:
# feat: complete day24 polymorphism assignment
# -------------------------
