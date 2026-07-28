# Day25 Assignment - Abstract Class

from abc import ABC, abstractmethod

# 1.
# Device를 추상 클래스(Abstract Class)로 만드세요.


class Device(ABC):
    # 2.
    # connect()를 추상 메서드(Abstract Method)로 만드세요.
    @abstractmethod
    def connect(self):
        pass


# 3.
# CiscoDevice를 만드세요.
# Device를 상속받으세요.
# connect()를 구현하여
# "Cisco NX-OS Connected"
# 를 출력하세요.


class CiscoDevice(Device):
    def connect(self):
        print("Cisco NX-OS Connected")


# 4.
# AristaDevice를 만드세요.
# Device를 상속받으세요.
# connect()를 구현하여
# "Arista EOS Connected"
# 를 출력하세요.


class AristaDevice(Device):
    def connect(self):
        print("Arista EOS Connected")


# 5.
# 객체를 생성하고 connect()를 호출하세요.

leaf1 = CiscoDevice()
spine1 = AristaDevice()

leaf1.connect()
spine1.connect()


# 6. (생각 문제)

# 왜 아래 코드는 오류가 발생할까요?

# device = Device()

# 자신의 생각을 주석으로 작성하세요.

"""
Device()은 connect()를 구현 하지 않아서
"""

# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day25-abstract-class
#
# Commit:
# feat: complete day25 abstract class assignment
# -------------------------
