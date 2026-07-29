def build_profile(name, job, goal):
    return f'''
====================
Who are you?
====================
Name: {name}
Role: {job}
Goal: {goal}
===================='''

name = input("Enter your name: ")
job = input("Enter your carrer: ")
goal = input("Enter your goal: ")

print(build_profile(name, job, goal))
