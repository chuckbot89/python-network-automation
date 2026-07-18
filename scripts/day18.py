# =========================================================
# Day 18 Final Assignment
# Topic:
# Object, Reference, Mutable, Immutable,
# Shallow Copy, Deep Copy
#
# GitHub
#
# Branch
# feature/day18-copy
#
# Commit
# feat: complete day18 shallow and deep copy assignment
# =========================================================


# -------------------------------
# Assignment 1
# -------------------------------

a = [["Cisco"]]

b = a.copy()

b.append(["Juniper"])

print(a)
print(b)

"""
질문

1. print(a)
- ["Cisco"]
2. print(b)
- ["Cisco", "Juniper"]
3. 왜 a는 바뀌지 않았을까?
- b.append(["Juniper"])는 b객체에 있는 outer list에 "Juniper"를 추가 했기 때문에 a는 변하지 않는다
4. append()가 수정한 객체(Object)는 무엇인가?
- b의 outer list
"""


# -------------------------------
# Assignment 2
# -------------------------------

a = [["Cisco"]]

b = a.copy()

b[0].append("Juniper")

print(a)
print(b)

"""
질문

1. print(a)
- ["Cisco", "Juniper"]
2. print(b)
- ["Cisco", "Juniper"]
3. append()는 어떤 객체(Object)를 수정했는가?
- inter list를 수정
4. 왜 a도 변경되었는가?
- inter list는 a와 b 모두다 reference 하고 있기 때문
"""


# -------------------------------
# Assignment 3
# -------------------------------

import copy

a = [["Cisco"]]

b = copy.deepcopy(a)

b[0].append("Juniper")

print(a)
print(b)

"""
질문

1. print(a)
- ["Cisco"]
2. print(b)
- ["Cisco", "Juniper"]
3. deepcopy()는 어떤 객체들을 새로 만들었는가?
- [["Cisco", "Juniper"]]
4. shallow copy와 가장 큰 차이는 무엇인가?
- shallow copy는 outer list만 copy 하고 inter list는 reference 하는 반면에 deepcopy는 inter list까지 copy 한다 if 객체가 immutable이라면
"""


# -------------------------------
# Assignment 4
# -------------------------------

device = {"Cisco": ["R1"]}

backup = device.copy()

backup["Cisco"] = ["R2"]

print(device)
print(backup)

"""
질문

1. print(device)
- "Cisco": ["R2"]
2. print(backup)
- "Cisco": ["R2"]
3. 기존 List를 수정한 것인가?
- 기존 List를 수정햇어. R1 -> R2로 overwrite했어.
4. 새로운 List를 만든 것인가?
- No
5. Dictionary에서 무엇이 변경되었는가?
- Cisco key에 대한 value "R2"로 update
"""


# -------------------------------
# Assignment 5
# -------------------------------

device = {"Cisco": ["R1"]}

backup = device.copy()

backup["Cisco"].append("R2")

print(device)
print(backup)

"""
질문

1. print(device)
- "Cisco": ["R1", "R2"]
2. print(backup)
- "Cisco": ["R1", "R2"]
3. 왜 둘 다 변경되었는가?
- device와 backup은 같은 객체를 reference하고 있기 때문
4. 어떤 객체(Object)를 공유하고 있었는가?
- "Cisco": ["R1"]
"""


# -------------------------------
# Assignment 6
# -------------------------------

device = {"Cisco": ["R1"]}

backup = copy.deepcopy(device)

backup["Cisco"].append("R2")

print(device)
print(backup)

"""
질문

1. print(device)
- "Cisco": ["R1"]
2. print(backup)
- "Cisco": ["R1", "R2"]
3. deepcopy()가 새로 생성한 객체(Object)는 무엇인가?
- "Cisco": ["R1"]
4. 왜 원본은 변경되지 않았는가?
- backup의 객체들이 새롭게 생성됬기 때문이야 "R1" str이기 때문에 immutable이여서 새로 생성돼
"""


# -------------------------------
# Assignment 7 (Memory Diagram)
# -------------------------------

a = {"Cisco": ["R1"]}

b = a.copy()

"""
Memory Diagram을 그려보세요.

- Dictionary는 몇 개인가?
- 2개
- List는 몇 개인가?
- 1개
- String은 몇 개인가?
- 1개
- 어떤 객체(Object)를 a와 b가 함께 참조하고 있는가?
- "Cisco": ["R1"]
"""


# -------------------------------
# Assignment 8 (Concept)
# -------------------------------

"""
아래 용어를 자신의 말로 설명하세요.

1. Object(객체)

2. Reference(참조)

3. Mutable(가변)

4. Immutable(불변)

5. Assignment(대입)

6. Reassignment(재할당)

7. Shallow Copy(얕은 복사)

8. Deep Copy(깊은 복사)

9. append()와
   a = a + [...] 의 차이

10. Python은 왜 deepcopy()를 만들었는가?
"""
