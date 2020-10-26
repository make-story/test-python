# -*- coding: utf-8 -*-

# 기본호출
def factorial(n):
    if n <= 1:
        return 1
print(factorial(0)) # 1
print(factorial(1)) # 1


# Iteration vs. Recursion
# 재귀호출
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5)) # 120
# 문제!
# 재귀호출을 반복(Iteration) 형태로 변환한 문제 
def factorial(n):
    result = 1
    # ---------- 
    for i in range(n):
        result = result * (i+1)
    # ---------- 
    return result
print(factorial(5)) # 120


# 문제!
def reversed2(s):
    # ---------- 
    if len(s) <= 1:
        return s
    return s[-1] + reversed2( s[1:-1] ) + s[0]
    # ---------- 

print( reversed2('abcde') ) # edcba
print( reversed2('Testing') ) # gnitseT


# 문제!
# 주어진 문자열이 회문(palindrome)인지 확인
# 앞뒤로 철자가 같은 경우 문자열은 회문입니다.
def remove_punc(s):
    result = ''
    for ch in s.lower(): # 대소문자 구분 없이
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            result += ch
    return result
def is_palindrome(s):
    # ---------- 
    if len(s) <= 1:
        return True
    else:
        return s[-1] == s[0] and is_palindrome( s[1:-1] )
    # ---------- 

palindrome_list = ['Wow',
    'Was it a cat I saw?',
    'A Santa at Nasa.',
    'No lemon, no melon',
    'Red rum, sir, is murder',
    'abcde']
 
for p in palindrome_list:
    print( '{} [{}]'.format(p, is_palindrome(remove_punc(p)) ) )

# Tower of Hanoi
# def print_hanoi():
#     print('{:10}{:10}{:10}'.format(str(source1), str(helper1), str(target1)) )
# def move(source, target):
#     target.append( source.pop() )
#     print_hanoi()
# def hanoi(n, source, helper, target):
#     if n > 0:
#         hanoi(n - 1, source, target, helper)
#         move(source, target)
#         hanoi(n - 1, helper, source, target)
# source1 = [3,2,1]
# target1 = []
# helper1 = []
# print_hanoi()
# hanoi( len(source1), source1, helper1, target1 )





# 파이썬 그래픽
# 트리 그리기
# import turtle
# import random
# def tree(t, blen):
#     if blen > 5:
#         t.forward(blen)
#         current_angle = t.heading()
#         t.setheading( current_angle + 20 )
#         tree(t, blen-15)
#         t.setheading( current_angle - 20 )
#         tree(t, blen-15)
#         t.setheading( current_angle )
#         t.backward(blen)
# t = turtle.Turtle()
# t.left(90)
# t.color('blue')
# tree(t, 75)
# turtle.exitonclick()
