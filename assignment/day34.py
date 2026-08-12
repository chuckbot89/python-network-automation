# Day34 Assignment - HTTP Method

import requests

# 1.
# 아래 Dictionary를 만드세요.

device = {"hostname": "Leaf1", "vendor": "Cisco"}


# 2.
# 아래 URL로 POST 요청을 보내세요.
#
# https://httpbin.org/post
#
# json=device
#
# 를 사용하세요.

url = "https://httpbin.org/post"
response = requests.post(url, json=device)

# 3.
# response.status_code를 출력하세요.

print(response.status_code)

# 4.
# response.json()을 출력하세요.

print(response.json())

# 5.
# 아래 URL로 PUT 요청을 보내세요.
#
# https://httpbin.org/put
#
# json=device
#
# 를 사용하세요.

url = "https://httpbin.org/put"
response = requests.put(url, json=device)

# 6.
# response.status_code를 출력하세요.

print(response.status_code)

# 7.
# 아래 URL로 DELETE 요청을 보내세요.
#
# https://httpbin.org/delete
#
# DELETE 요청을 보내세요.

url = "https://httpbin.org/delete"
response = requests.delete(url)
# 8.
# response.status_code를 출력하세요.

print(response.status_code)

# -------------------------
# 생각 문제
#
# 왜
#
# requests.post(..., json=device)
#
# 에서는
#
# Dictionary를 그대로 보낼 수 있을까요?
#
# 자신의 말로 설명하세요.

"""

Requests 라이브러리가 변환을 대신 해주기 때문

"""

# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day34-http-method
#
# Commit:
# feat: complete day34 http methods assignment
