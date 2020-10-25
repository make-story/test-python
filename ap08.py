# -*- coding: utf-8 -*-

class Pet:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    def play(self): # 메서드
        print(self.name + 'is playing...')
    def sleep(self): # 매서드
        print(self.name + 'is sleeping...')

p1 = Pet('개', '코코',2) 
p2 = Pet('고양이', '보리',3) 
p3 = Pet('거북이', '콩이',20)
if p3.age > p1.age and p3.age > p2.age:
    print( '{} is older than {} and {}'.format( p3.name, p1.name, p2.name ) ) # 콩이 is older than 코코 and 보리


# 상속
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Dog(Pet):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color

yomi = Pet( '요미', '5살' )
#sofia = Dog( '소피아', '4살', '흰색' )
print( 'Pet: {} {}'.format(yomi.age, yomi.name) ) # Pet 5살 요미
#print( 'Dog: {} {} {} 개'.format(sofia.age, sofia.name, sofia.hair_color) ) # 4살 소피아 흰색 개


# 매직메서드
class Dog:
    def __init__(self, age):
        self.age = age
    def __len__(self): # 매직메서드 : len() 호출시
        return self.age
joy = Dog(3)
print( len( joy ) ) # __len__ 호출

class Grade:
    def __init__(self, grade):
        self.grade_index = 'ABCDF'.find(grade)
    def __add__(self, num): # 매직메서드 : "+" 호출시
        self.grade_index = self.grade_index - num
        if self.grade_index > 4: self.grade_index = 4
        if self.grade_index < 0: self.grade_index = 0
        return self 
    def __str__(self): # 매직메서드 : str() or print() 호출시 
        return 'ABCDF'[self.grade_index]
    def __eq__(self, other): # 매직메서드 : "==" 사용시 
        return self.grade_index == other.grade_index

g1 = Grade('A')
g2 = Grade('F')
print(g1 + -2 == g2 + 2 )
print(g1 + -3 == g2 + 3 )