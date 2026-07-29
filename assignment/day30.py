# Day30 Assignment - Package


# 프로젝트 구조를 만드세요.
#
# automation/
#
# ├── main.py
#
# ├── backup/
# │   ├── __init__.py
# │   ├── nxos.py
# │   └── eos.py


# ----------------------------
# backup/nxos.py
#
# backup(device) 함수를 작성하세요.
#
# 출력:
#
# NX-OS Backup: Leaf1


# ----------------------------
# backup/eos.py
#
# backup(device) 함수를 작성하세요.
#
# 출력:
#
# EOS Backup: Leaf2


# ----------------------------
# main.py
#
# 두 backup() 함수를 import 하세요.
#
# 함수 이름이 겹치므로
#
# as
#
# 를 사용하여 별칭(Alias)을 지정하세요.
#
# 예)
#
# nxos_backup(...)
# eos_backup(...)
#
# 를 호출하세요.


# ----------------------------
# 생각 문제
#
# 왜
#
# from backup.nxos import backup
#
# 처럼
#
# 점(.)
#
# 을 사용할까요?
#
# 자신의 말로 주석으로 작성하세요.


# ----------------------------
# GitHub Workflow
#
# Branch:
# feature/day30-package
#
# Commit:
# feat: complete day30 package assignment
# ----------------------------
