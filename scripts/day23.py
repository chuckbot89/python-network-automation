# Day23 Assignment - super()


class Device:
    def __init__(self, hostname):
        self.hostname = hostname

    def show_info(self):
        print(f"Hostname: {self.hostname}")


# 1.
# Device를 상속받는 CiscoDevice 클래스를 만드세요.


class CiscoDevice(Device):
    # 2.
    # CiscoDevice의 __init__()에서
    # super().__init__(hostname)을 호출하세요.

    # 그리고 self.version을 추가하세요.

    def __init__(self, hostname, version):
        self.version = version
        super().__init__(hostname)

    # 3.
    # show_info()를 오버라이딩하세요.

    def show_info(self):
        print(f"Hostname: {self.hostname} Version: {self.version}")


# 먼저 부모의 show_info()를 실행한 후
# Version: {self.version}
# 을 출력하세요.

hostname = "Default_device1"

device = Device(hostname)
device.show_info()

# 4.
# 객체를 생성하세요.

hostname = "Leaf1"
version = "10.3"

device = CiscoDevice(hostname, version)

# 5.
# show_info()를 호출하세요.

device.show_info()

# 6. (생각 문제)

# super().__init__(hostname)

# 은 새로운 Device 객체를 만드는 것일까요?

# 아니라면 무엇을 하는 것일까요?


# GitHub

# Branch
# feature/day23-super

# Commit
# feat: use super in inheritance
