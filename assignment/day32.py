# Day32 Assignment - Requests

import requests

# 1.
# 아래 URL로 GET 요청을 보내세요.
#
# https://httpbin.org/get


# 2.
# Response 객체를
#
# response
#
# 변수에 저장하세요.

response = requests.get("https://httpbin.org/get")

# 3.
# 다음을 출력하세요.
#
# response.status_code

print(response.status_code)

# 4.
# 다음을 출력하세요.
#
# type(response)

print(type(response))

# 5.
# response.json()을 호출하여
#
# data
#
# 변수에 저장하세요.

data = response.json()

# 6.
# type(data)를 출력하세요.

print(type(data))

# 7.
# data를 출력하세요.

print(data)

# -------------------------
# 생각 문제
#
# response는 왜 Dictionary가 아니라
#
# Response 객체(Object)일까요?
#
# 자신의 생각을 주석으로 작성하세요.
#
"""
response는 HTTP 응답 전체를 표현하는 객체이다.

HTTP 응답에는 status_code, headers, text, cookies 등
여러 속성과 메서드가 필요하므로 Dictionary가 아니라
Response 객체로 설계되어 있다.

response.json()을 호출하면
그때 JSON 데이터를 새로운 Dictionary 객체로 변환하여 반환한다.
"""
# -------------------------
#
# GitHub Workflow
#
# Branch:
# feature/day32-requests
#
# Commit:
# feat: complete day32 requests assignment
#
# -------------------------
