# =========================================================
# Day35 Assignment
# Topic:
# HTTP Header & Authentication
#
# GitHub
#
# Branch
# feature/day35-auth
#
# Commit
# feat: complete day35 header and authentication assignment
# =========================================================

import requests

# -------------------------------
# Assignment 1
# -------------------------------

url = "https://httpbin.org/headers"

# headers Dictionary를 만드세요.
#
# Accept:
# application/json
#
# X-Device:
# Leaf1

headers = {"Content-Type": "application/json", "X-Device": "Leaf1"}

# requests.get()을 사용하여
# headers를 서버로 보내세요.

response = requests.get(url, headers=headers)

# response.status_code를 출력하세요.

print(response.status_code)

# response.json()을 출력하세요.

print(response.json())

# -------------------------------
# Assignment 2
# -------------------------------

url = "https://httpbin.org/basic-auth/admin/cisco"

# Basic Authentication을 사용하세요.
#
# username:
# admin
#
# password:
# cisco
#
# 힌트:
#
# auth=(..., ...)

# GET 요청을 보내세요.

response = requests.get(url, auth=("admin", "cisco"))

# response.status_code를 출력하세요.

print(response.status_code)

# response.raise_for_status()를 호출하세요.

response.raise_for_status()

# -------------------------------
# Assignment 3
# -------------------------------

token = "abc123"

url = "https://httpbin.org/headers"

# 다음 Header를 만드세요.
#
# Authorization:
# Bearer abc123
#
# 단, token 변수를 사용하세요.

headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

# GET 요청을 보내세요.

response = requests.get(url, headers=headers)

# response.json()을 출력하세요.

print(response.json())

# -------------------------------
# 생각 문제
# -------------------------------

# 다음 네 가지가 각각 무엇을 의미하는지
# 자신의 말로 설명하세요.
#
# 1. HTTP Method
# - 리소스(Resource)에 어떤 동작(Operation)을 요청할 것인지 나타낸다.
# 2. URL
# - 어디에 할껀지
# 3. Header
# - 요청에 관한 메타데이터(Metadata)
# 4. Body
# - 서버에 실제로 전달할 데이터(Payload)가 들어가는 부분
#
# 추가 질문:
#
# Authentication과 Authorization은
# 어떤 차이가 있을까요?
#
# 자신의 말로 작성하세요.

"""

authentication은 서버가 내가 누구인지 확인 Authorization은 무엇을 할수 있는지에 대한 권한을 확인

"""
