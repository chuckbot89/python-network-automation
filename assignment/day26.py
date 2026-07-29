# Day26 Assignment - Exception Handling


# 1.
numbers = [10, 5, 0, 2]
#
# 반복문을 사용하여
# 100 / number 를 출력하세요.
#
# 단,
# 0으로 나누는 경우에는
#
# "Cannot divide by zero."
#
# 를 출력하고
# 다음 반복을 계속 진행하세요.

for number in numbers:
    try:
        print(100 / number)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

# 2.
# ZeroDivisionError as e
#
# 를 사용하여
#
# 오류 메시지도 함께 출력하세요.

for number in numbers:
    try:
        print(100 / number)

    except ZeroDivisionError as e:
        print(e)

# 3.
# 마지막에
#
# "Program Finished"
#
# 를 출력하세요.

for number in numbers:
    try:
        print(100 / number)

    except ZeroDivisionError as e:
        print(f"Connection Failed: {e}")

print("Program Finished")

# 4. (생각 문제)
#
# 왜 try를 사용하지 않으면
# 반복문이 끝까지 실행되지 않을까요?
#
# 자신의 생각을 주석으로 작성하세요.

"""
normal behavior는 오류가 나면 프로그램이 종료 되서 끝까지 실행 되지 않아.
"""

# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day26-exception-handling
#
# Commit:
# feat: complete day26 exception handling assignment
# -------------------------
