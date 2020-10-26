# -*- coding: utf-8 -*-


# find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
# rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
print("안녕하세요".find("안녕")) # 0
print("안녕안녕하세요".rfind("안녕")) # 2

# 문제!  
for i in range(10):
    print('*' * (i+1))
for i in range(10):
    print(' ' * (i+1) + '*' * (9-i))


# 문제! - 숫자 문제형으로 변환후 결합!
str1 = 'He is '
str2 = 60
str3 = ' years old.'
print(str1 + str(str2) + str3)


# 0 1 2 3 4 5
# P y t h o n
# -5 -4 -3 -2 -1
str1 = 'Python'
print(str1[-1])

singers = "Peter, Paul, and Mary"
# [start index : end index : step index]
print(singers[0:5]) # Peter
print(singers[7:11]) # Paul
print(singers[17:21]) # Mary

fruit = "banana"
print(fruit[:3]) # ban 
print(fruit[3:]) # ana
print(fruit[3:-10]) # 
print(fruit[3:99]) # ana
# 문제!
print(fruit[::2]) # bnn - 세번째는 step size


# Printing without a Newline
# this is default behavior
#print("my string", end="\n")
# print string without a newline
#print("my string", end="")
# now print() will print foo after every string
#print("my string", end="foo")


# 중요 문제!
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit :
    print(letter)


fruit = 'banana'
for i in range(len(fruit)):
    print(i, fruit[i])


# 중요! enumerate()
for item in enumerate(fruit):
    print(item)

for item in enumerate(fruit):
    print(item[0], item[1])

for i, ch in enumerate(fruit):
    print( i, ch )


# 문자열을 변경 못한다
#greeting = "Hello, world!"
#greeting[0] = 'J'            # ERROR!
#print(greeting)
# 문자열 변경 방법
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)

# 문자열 관련 함수 조회
#dir(str)

s = "welcome to python"
s.endswith("thon")
# True
s.startswith("good")
# False
s.find("come")
# 3
s.find("become")
# -1
s.rfind("o")
# 15
s.count("o")
# 3


s = "string in python"
s1 = s.capitalize()
# 'String in python'
s2 = s.title()
# 'String In Python'

s = "This Is Test"
s3 = s.lower()
# 'this is test'
s4 = s.upper()
# 'THIS IS TEST'
s6 = s.replace("Is", "Was")
# 'This Was Test'

greet = '   Hello Bob  '
greet.lstrip()
# 'Hello Bob  '
greet.rstrip()
# ' Hello Bob'
greet.strip()
# 'Hello Bob'