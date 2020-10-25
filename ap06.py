# -*- coding: utf-8 -*-

# 중요!
# [ expression for item in list if conditional ]

# Slicing
# [ start : stop : step ]
x = 'computer'
x[1:4]   # Items 1 to 3 : 출력 'omp'
x[1:6:2] # Items 1, 3, 5 : 출력 'opt'
x[3:]    # Items 3 to end : 출력 'puter'
x[:5]    # Items 0 to 4 : 출력 'compu'
x[-1]    # Last item : 출력 'r'
x[-3:]   # Last 3 items : 출력 'ter'
x[:-2]   # All except last 2 items : 출력 'comput'

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



# list
# del list1[2] 
# list1.append(item) 
# list1.extend(sequence1) 
# list1.pop() 
# list1.remove(item) 
# list1.reverse() 
# list1.sort()
x = []
x = [3, 4, 5]
x = [n for n in range(5)]
x = list()
x = list(range(5))

# List Comprehension
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

# pop
# 문제!
x = [3, 5, 7, 9]
print(x.pop()) # 9
print(x.pop(2)) # 7
print(x) # [3, 5]

# remove()
x = [3, 5, 7, 9]
x.remove(7)
print(x) # [3, 5, 9]
# 문제!
#x = [3, 5, 7, 9]
#x.remove(11) # ValueError: list.remove(x): x not in list
#print(x) 

# reverse()
x = [3, 5, 7, 9]
x.reverse()
print(x) # [9, 7, 5, 3]
# 문제!
x = [3, 5, 7, 9]
print(x.reverse()) # None
print(x[::-1]) # [3, 5, 7, 9]

# sort()
x = [93, 3, 17, 11]
x.sort() # [3, 11, 17, 93]
print(x)
# 문제! sorted(x) returns a new sorted list without changing the original list x.
x = [93, 3, 17, 11]
sorted(x)
print(x)

# split()
text1 = 'everybody has a plan'
print( text1.split() )
text2 = 'everybody, has, a, plan'
print( text2.split(', ') )
# 문제!
text1 = 'dog;cat,monkey;bird,fish' 
print( text1.split(';') ) # ['dog', 'cat,monkey', 'bird,fish']
text2 = 'hello      world  !!!'
print( text2.split() ) # ['hello', 'world', '!!!']

# 튜플
x = ()
print(len(x)) # 0
x = ('hello',)
print(len(x)) # 1
x = ('hello') # not tuple
print(len(x)) # 5

# Tuple Packing
t = 12345, 54321, 'hello!'
print(t)

# Tuple Unpacking
(x, y, z) = (12345, 54321, 'hello!')
a, b, c = 32, 44, 99
q, p = [100, 200]
print(z)
print(q)
print(c)


# Creating a New Dictionary
d = {}
d = dict()
d = {'pork': 25.3, 'beef': 33.8, 'chicken':22.7}
d = {x: x**2 for x in (2, 4, 6)}

# Dictionary Comprehension
d = { x:x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}

# 딕셔너리 테스트
counts = {}
names=['영구','길동','일등','길동','일등','일등','기동','농민'] 
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] += 1
print(counts) # {' ':1,' ':3,' ':3,' ':1}

# key, value, 튜플
d = {'pork': 25.3, 'beef': 33.8, 'chicken':22.7}
print( list(d.keys()) )  # list of keys : 출력 ['pork', 'beef', 'chicken']
print( list(d.values()) )  # list of values : 출력 [25.3, 33.8, 22.7]
print( list(d.items()) )  # list of key-value tuple pairs : 출력 [('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)]

# 문제!
d = {'pork': 25.3, 'beef': 33.8, 'chicken':22.7}
print(list(d)) # ['pork', 'chicken', 'beef']
print(sorted(list(d))) # ['beef', 'chicken', 'pork']
# ----------
l = sorted(list(d))
for i, key in enumerate(l):
    print( i, d[key] )
# ----------
# 0 33.8
# 1 22.7
# 2 25.3
