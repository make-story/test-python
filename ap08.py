# -*- coding: utf-8 -*-

class Pet:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    def play(self):
        print(self.name + 'is playing...')
    def sleep(self):
        print(self.name + 'is sleeping...')

p1 = Pet('개', '코코',2) 
p2 = Pet('고양이', '보리',3) 
p3 = Pet('거북이', '콩이',20)
if p3.age > p1.age and p3.age > p2.age:
    print( '{} is older than {} and {}'.format( p3.name, p1.name, p2.name ) ) # 콩이 is older than 코코 and 보리