# Day28 Assignment - File I/O


# 1.
# devices 리스트를 만드세요.
#
devices = ["Leaf1", "Leaf2", "Spine1"]


# 2.
# with open()을 사용하여
#
# devices.txt
#
# 파일을 쓰기 모드("w")로 여세요.

with open("./data/devices.txt", "w") as file:
    file.writelines(device + "\n" for device in devices)

# 3.
# 반복문을 사용하여
#
# 각 장비 이름을
#
# 한 줄씩 저장하세요.


# 4.
# 다시
#
# with open()
#
# 으로 읽기 모드("r")로 파일을 여세요.

with open("./data/devices.txt", "r") as file:
    print(file.readlines())

# 5.
# 파일 내용을 읽어서 출력하세요.


# 6. (생각 문제)
#
# 왜 실무에서는
#
# open()
# ...
# close()
#
# 보다
#
# with open()
#
# 을 더 많이 사용할까요?
#
# 자신의 생각을 주석으로 작성하세요.


# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day28-file-io
#
# Commit:
# feat: complete day28 file io assignment
# -------------------------
