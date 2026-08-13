# =========================================================
# Day36 Assignment
# Topic:
# Token Authentication
#
# GitHub
#
# Branch
# feature/day36-token-auth
#
# Commit
# feat: complete day36 token authentication assignment
# =========================================================

import requests

# -------------------------------
# Assignment 1
# -------------------------------

# 다음 Dictionary를 만드세요.
#
# username: admin
# password: cisco

auth = {"username": "admin", "password": "cisco"}

# -------------------------------
# Assignment 2
# -------------------------------

# 로그인 URL
#
# https://example.com/login
#
# 이 있다고 가정하세요.
#
# requests.post()를 사용하여
# credentials를 JSON Body로 보내는 코드를 작성하세요.
#
# 주의:
# 실제로 요청을 실행하지 않도록
# requests.post() 코드는 주석 처리하세요.

url = "https://example.com/login"
# response = requests.post(url, auth)

# -------------------------------
# Assignment 3
# -------------------------------

# 서버에서 response.json()을 실행한 결과가
# 다음과 같다고 가정하세요.

data = {"token": "abc123"}

# data에서 token 값을 가져와
# token 변수에 저장하세요.

token = data["token"]

# -------------------------------
# Assignment 4
# -------------------------------

# 다음 HTTP Header를 만드세요.
#
# Authorization: Bearer abc123
# Accept: application/json
#
# 단, 위에서 만든 token 변수를 사용하세요.

headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

# -------------------------------
# Assignment 5
# -------------------------------

device_url = "https://example.com/devices"

# requests.get()을 사용하여
# 위에서 만든 headers를 전달하는 코드를 작성하세요.
#
# 실제 요청은 실행하지 않도록 주석 처리하세요.

response = requests.get(device_url, headers=headers)

# -------------------------------
# 생각 문제
# -------------------------------

# 다음 흐름을 자신의 말로 설명하세요.
#
# credentials
#     ↓
# POST /login
#     ↓
# response
#     ↓
# response.json()
#     ↓
# token
#     ↓
# headers
#     ↓
# GET /devices
#
#
# 추가 질문:
#
# token = data["token"]
#
# 에서
#
# data는 어떤 객체(Object)이고,
# token은 어떤 객체(Object)를 참조할까요?
