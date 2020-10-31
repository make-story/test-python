
# 중요!


# 리스트 내포 - List Comprehension
# [ expression for item in list if conditional ]
# 변수 = [표현식/반환값 for 반복자 in 반복할 수 있는 것/리스트 if 조건문]
arr = ["사과", "자두", "초콜릿"]
out = [fruit for fruit in arr if fruit != "초콜릿"]
print(out) # ['사과', '자두']

# [:::] 범위 선택자 (슬라이싱) slicing
# [ start : end : step ]
# step이 양수일 때: 오른쪽으로 step만큼 이동하면서 가져옵니다.
# step이 음수일 때: 왼쪽으로 step만큼 이동하면서 가져옵니다.

# range(시작, 종료, 간격/범위) 
# 종료값이 출력되도록 원한다면 "종료값-1"
# list(range(10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(5, 10)) # [5, 6, 7, 8, 9]
# list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
# list(range(0, 10 + 1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list(range(10, 0-1, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# Concatenating
name = 'Hong' + 'Gil' + 'Dong'
print(name) # HongGilDong
items1 = [1,3,5,7] + [2,4,6,8]
print(items1) # [1, 3, 5, 7, 2, 4, 6, 8]
items2 = ['a', 50, 'abc'] + [0.2, 5, 'e']
print(items2) # ['a', 50, 'abc', 0.2, 5, 'e']


# Repeating
x = 'bug' * 3
print(x) # bugbugbug
x = [3, 4] * 3 
print(x) # [3, 4, 3, 4, 3, 4]
# 문제!
x = [[1,2],[3,4]] * 2
print(x) # [[1, 2], [3, 4], [1, 2], [3, 4]]


# Checking Membership
x = 'u' in 'bug'
print(x) # True
x = 'cow' in ['pig', 'dog', 'cow']
print(x) # true
# 문제!
x = 'cow' in ['pig', 'dog', ['cow', 'cat', 'bird'] ]
print(x) # False


# Iterating
x = [3, 5, 1]
print(range(len(x))) # [0, 1, 2]
for i in range(len(x)):
    print(x[i] * 2) # 첫번째 반복 : 6, 두번째 반복 : 10, 세번째 반복 : 2


# Iterating
x = ['b', 'a', 'e']
for (index, item) in enumerate(x):
    print(index, item) # 첫번째 반복 : (0, 'b'), 두번째 반복 : (1, 'a'), 세번째 반복 : (2, 'e')


# Number of items
x = 'bug'
print(len(x)) # 3
x = [4, 6, 2, 4]
print(len(x)) # 4
# 문제!
x = [4, 6, 2, [ 3, 2, ['a', 'b', 'c'] ] ]
print(len(x)) # 4


# count ( item ) method
x = 'awesome'
print(x.count('e')) # 2
x = ['dog', 'cat', 'horse', 'cat', 'cat']
print(x.count('cat')) # 3
# 문제!
x = ['dog', 'cat', 'horse', ['cat', 'cat'] ]
print(x.count('cat')) # 1


# index ( item ) method
x = 'awesome'
print(x.index('e')) # 2
x = ['dog', 'cat', 'horse', 'cat', 'cat']
print(x.index('cat')) # 1
# 문제!
x = ['dog', 'cat', 'horse', 'cat', 'cat']
#print(x.index('hat')) # ValueError: 'hat' is not in list


# List Comprehension (리스트 내포)
# 기존방식
new_list = []
for i in range(10):
    new_list.append( i )
# List Comprehension 방식
new_list = [ i for i in range(10) ]
print(new_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 기존방식
new_list = []
for i in range(10):
    if i > 3:
        new_list.append( i*i )
# List Comprehension 방식
new_list = [ i*i for i in range(10) if i > 3 ] # [리턴값 for 반복문 if 조건]
print(new_list) # [16, 25, 36, 49, 64, 81]

# 리스트 반대로
for i in range(4, 0-1, -1):
    print("현재변수 반복: {}".format(i)) # 4 3 2 1 0





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



########################################
# • string slicing 문제
########################################

# Slicing
# [:::] 범위 선택자 (슬라이싱) slicing
# [ start : end : step ]
# step이 양수일 때: 오른쪽으로 step만큼 이동하면서 가져옵니다.
# step이 음수일 때: 왼쪽으로 step만큼 이동하면서 가져옵니다.

x = 'computer'
x[1:4]   # Items 1 to 3 : 출력 'omp'
x[1:6:2] # Items 1, 3, 5 : 출력 'opt'
x[3:]    # Items 3 to end : 출력 'puter'
x[:5]    # Items 0 to 4 : 출력 'compu'
x[-1]    # Last item : 출력 'r'
x[-3:]   # Last 3 items : 출력 'ter'
x[:-2]   # All except last 2 items : 출력 'comput'

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


########################################
# • recursion (재귀)방식으로 자연수 곱셈 a × b 를 계산하는 함수 (iteration이나 단순 * 연산이 아닌)
########################################

# 재귀호출을 반복(Iteration) 형태로 변환한 문제 
def factorial(n):
    result = 1
    # ---------- 
    for i in range(n):
        result = result * (i+1)
    # ---------- 
    return result
print(factorial(5)) # 120

def reversed2(s):
    # ---------- 
    if len(s) <= 1:
        return s
    return s[-1] + reversed2( s[1:-1] ) + s[0]
    # ---------- 

print( reversed2('abcde') ) # edcba
print( reversed2('Testing') ) # gnitseT

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





########################################
# • 대소문자를 구별하지 않도록 하는 만드는 코드
########################################

s = "This Is Test"
s3 = s.lower()
# 'this is test'
s4 = s.upper()

greet = '   Hello Bob  '
greet.lstrip()
# 'Hello Bob  '
greet.rstrip()
# ' Hello Bob'
greet.strip()
# 'Hello Bob'


if haystackstr.lower().find(needlestr.lower()) != -1:
  # True

a = "MandY"
alow = a.lower()
if "mandy" in alow:
    print "true"

string1 = "hi"
string2 = "HI"
if string1.lower() == string2.lower():
    print "Equals!"
else:
    print "Different!"
    

########################################
# • 어떤 이름이 문자열 안에 존재하는지 확인하는 코드
########################################

# find() : 왼쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
# rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.
print("안녕하세요".find("안녕")) # 0
print("안녕안녕하세요".rfind("안녕")) # 2

# 대소문자 구분? 구분한다.
s = "welcome to python"
s.endswith("thon") # True
s.startswith("good") # False
s.find("come") # 3
s.find("become") # -1
s.rfind("o") # 15
s.count("o") # 3

########################################
# • nested(중첩) <-> chained conditional (체인조건부) 변환
# https://sites.google.com/a/lps.k12.co.us/ahs-intro-to-computer-science/home/selection/4-unary-selection
########################################


# Nested Conditionals
x = 10
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")

# Chained Conditionals
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")




########################################
# • 반복문 사용 방식 (for 예시 하나 주고 다른 방식으로 변경)
# while, 이터레이터, 제너레이터
########################################

# len()
# range()
# enumerate()

# 리스트 내포 - List Comprehension
# [ expression for item in list if conditional ]
# 변수 = [표현식/반환값 for 반복자 in 반복할 수 있는 것/리스트 if 조건문]
arr = ["사과", "자두", "초콜릿"]
out = [fruit for fruit in arr if fruit != "초콜릿"]
print(out) # ['사과', '자두']

l = [1, 2, 1, 2]
value = 2
while value in l:
    l.remove(value)
print(l) # [1, 1]

# while break / continue 사용가능


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

