# Day27 Assignment - raise


# 1.
# check_vlan() 함수를 만드세요.
#
# 매개변수(Parameter):
# vlan
#
# VLAN이 1보다 작으면
#
# raise ValueError("Invalid VLAN ID")
#
# 를 발생시키세요.
#
# 그렇지 않으면
#
# "VLAN {vlan} configured."
#
# 를 출력하세요.


def check_vlan(vlan):

    if vlan < 1:
        raise ValueError("Invalid VLAN ID")

    else:
        print(f"VLAN {vlan} configured.")


# check_vlan(2)

# 2.
# try / except를 사용하여
#
# check_vlan(-10)
#
# 을 호출하세요.
#
# 오류 메시지를 출력하세요.


def check_vlan(vlan):

    try:
        if vlan < 1:
            raise ValueError("Invalid VLAN ID")

        else:
            print(f"VLAN {vlan} configured.")

    except ValueError as e:
        print(e)


check_vlan(-1)

# 3.
# 다시
#
# check_vlan(100)
#
# 을 호출하세요.
#
# 정상적으로 출력되는지 확인하세요.

check_vlan(100)

# 4. (생각 문제)
#
# raise를 사용하는 이유는 무엇일까요?
#
# 단순히 print("Invalid VLAN")을 하는 것과
# 어떤 차이가 있을까요?
#
# 자신의 생각을 주석으로 작성하세요.

"""
raise를 사용 하면 내가 원하는 곳에 예외 처리를 발생 시켜서 프로그램을 종료 시킬수 있어
"""

# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day27-raise
#
# Commit:
# feat: complete day27 raise assignment
# -------------------------
