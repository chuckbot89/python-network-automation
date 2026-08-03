# Day33 Assignment - Status Code
import requests

url = "https://httpbin.org/status/200"

# 1.
# GET 요청을 보내세요.

response = requests.get(url)

# 2.
# response.status_code를 출력하세요.

print(response.status_code)

# 3.
# response.ok를 출력하세요.

print(response.ok)

# 4.
# response.raise_for_status()를 호출하세요.

response.raise_for_status()

# 5.
# 아래 URL로 변경하세요.
#
# https://httpbin.org/status/404
#
# 그리고 try/except를 사용하여
#
# HTTPError를 출력하세요.

url = "https://httpbin.org/status/404"

try:
    response = requests.get(url)

    response.raise_for_status()

    print(response.json())

except requests.HTTPError as e:
    print(e)

# -------------------------
# 생각 문제
#
# 왜
#
# response.raise_for_status()
#
# 를 사용하는 것이
#
# if response.status_code != 200
#
# 보다 실무에서 더 많이 사용될까요?
#
# 자신의 말로 작성하세요.

"""
response.raise_for_status()는 HTTP 오류를 자동으로
HTTPError 예외로 변환해 준다.

그래서 try/except를 이용한 예외 처리와
자연스럽게 연결할 수 있고,
상태 코드를 직접 하나씩 검사하는 것보다
코드가 간결하고 유지보수가 쉽다.
"""

# -------------------------
# GitHub Workflow
#
# Branch:
# feature/day33-status-code
#
# Commit:
# feat: complete day33 response status assignment
# -------------------------
