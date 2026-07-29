# Day19 Assignment - Method

# 1.
# 아래 Device 클래스를 완성하세요.


class Device:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def show_info(self):
        # hostname과 ip를 출력하세요.
        print(f"{self.hostname}: {self.ip}")


# 2.
# 아래 객체를 생성하세요.

leaf1 = Device("Leaf1", "10.1.1.1")
leaf2 = Device("Leaf2", "10.1.1.2")


# 3.
# 각 객체에서 show_info()를 호출하세요.
leaf1.show_info()
leaf2.show_info()

# 4.
# 아래 메서드를 추가하세요.


class Device:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def show_info(self):
        print(f"{self.hostname}: {self.ip}")

    def change_ip(self, new_ip):
        # self.ip를 new_ip로 변경하세요.
        self.ip = new_ip


leaf1 = Device("Leaf1", "10.1.1.1")
leaf2 = Device("Leaf2", "10.1.1.2")


# 5.
# leaf1의 IP를 10.1.1.100으로 변경한 뒤,
# show_info()를 다시 호출하여 변경되었는지 확인하세요.

leaf1.change_ip("10.1.1.100")

leaf1.show_info()

# GitHub

# Branch
# feature/day19-method

# Commit
# feat: implement device methods
