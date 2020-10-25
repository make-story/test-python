# -*- coding: utf-8 -*-
import re
text = '"안녕하세요, 반값습니다!"'
exp = r'\w+' # \w : word 를 표현하며 알파벳 + 숫자 + _ 중의 한 문자임을 의미한다.
print( re.findall( exp, text ) ) # 결과 : []


text = '"안녕하세요, 반값습니다!"'
exp = r'\W+' # \W : non word를 표현하며 알파벳 + 숫자 + _ 가 아닌 문자를 의미한다. 
print( re.findall( exp, text ) )

# 대 소문자 구별하지 않는 정규식
# 암호가 6-12 개의 소문자 영숫자로 구성되어 있는지 확인하려고합니다. 적절한 정규 표현식은 무엇입니까?

