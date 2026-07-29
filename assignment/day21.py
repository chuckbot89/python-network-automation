# Day21 Assignment - Inheritance


class Device:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def show_info(self):
        print(f"{self.hostname}: {self.ip}")


# 1.
# Device를 상속받는 CiscoDevice 클래스를 만드세요.


class CiscoDevice(Device):
    pass


# 2.
# CiscoDevice 객체를 생성하세요.

hostname = "Leaf1"
ip = "10.1.1.1"

leaf1 = CiscoDevice(hostname, ip)


# 3.
# show_info()를 호출하세요.

leaf1.show_info()

# 4.
# Device를 상속받는 AristaDevice 클래스도 만드세요.


class AristaDevice(Device):
    pass


# 5.
# AristaDevice 객체를 생성하고 show_info()를 호출하세요.

arista1 = AristaDevice(hostname, ip)

arista1.show_info()

# GitHub

# Branch
# feature/day21-inheritance

# Commit
# feat: implement class inheritance
