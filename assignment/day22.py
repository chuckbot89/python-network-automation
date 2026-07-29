# Day22 Assignment - Method Overriding


class Device:
    def __init__(self, hostname):
        self.hostname = hostname

    def show_vendor(self):
        print("Generic Device")

    def show_info(self):
        print(f"Hostname: {self.hostname}")


# 1.
# Device를 상속받는 CiscoDevice 클래스를 만드세요.


class CiscoDevice(Device):
    def show_vendor(self):
        print("Cisco NX-OS")


# show_vendor()를 오버라이딩하여
# "Cisco NX-OS"를 출력하세요.


# 2.
# Device를 상속받는 AristaDevice 클래스를 만드세요.


class AristaDevice(Device):
    def show_vendor(self):
        print("Arista EOS")


# show_vendor()를 오버라이딩하여
# "Arista EOS"를 출력하세요.


# 3.
# CiscoDevice 객체를 생성하세요.

hostname = "Leaf1"

cisco = CiscoDevice(hostname)

# 4.
# AristaDevice 객체를 생성하세요.

hostname = "Leaf2"

arista = AristaDevice(hostname)

# 5.
# 각 객체에서

cisco.show_info()
cisco.show_vendor()

arista.show_info()
arista.show_vendor()

# 를 호출하세요.


# 6. (생각 문제)

# 왜 show_info()는 부모(Device)의 메서드를 사용하고,

# show_vendor()는 자식(CiscoDevice, AristaDevice)의

# 메서드를 사용할까요?


# GitHub

# Branch
# feature/day22-method-overriding

# Commit
# feat: implement method overriding
