# 자료형 : 문자열, 숫자, 불
# 자료형 확인 : type()

# 여러줄 문자열 입력 : """ 끝따옴표 또는 작음따옴표 세번 반복
# 문자열 길이 : len()

# 연산자 우선 순위 : 곱셈과 나눗셈이 덧셈과 뺄샘보다 우선합니다. 또한, 곱셈/나눗셈과 덧셈/뺄샘처럼 같은 우선순위를 가지는 연산자는 왼쪽에서 오른쪽 순서로 계산합니다.

# 사용자로 부터 값 입력 : input()
# input() 함수는 사용자가 무엇을 입력해도 문자열 자료형

# 문자열을 숫자로 바꾸기 : int() 함수, float() 함수
# 숫자를 문자열로 바꾸기 : str()

# format() 함수 : 함수 앞쪽에 있는 문자열의 {} 기호가 format() 함수의 괄호 안에 있는 매개변수로 차례로 대치 (숫자값 입력시 문자열 타입이 됨)

# 대소문자 바꾸기 : upper() 함수, lower() 함수

# 문자열 양옆의 공백 제거 : strip()

# 문자열의 구성 파악 : is타입 (예: isalnum(), isalpha(), isdentifer() 등)

# 문자열 찾기 : find() 왼쪽부터 찾아서 처음 등장하는 위치, rfind() 오른쪽부터 찾아서 처음 등장하는 위치

# 문자열 자르기 : split(), 실행결과는 배열(리스트)

# 배열 인덱스 음수 : 뒤에서부터 요소를 선택, arr[-1] 배열의 맨마지막

# 배열 리스트의 요소 추가 : append, insert

# 배열 리스트 요소 제거 : del 리스트명[인덱스] 또는 리스트명.pop(인덱스)

# 배열 리스트 값으로 제거 : 리스트.remove(값)

# 배열 리스트 모두 제거 : 리스트.clear()

# 배열 리스트 내부 값 있는지 여부 : 값 in 리스트: (예: 273 in 리스트)

# for 반복문 : for 반복자 in 반복할 수 있는 것

array = [1, 2, 3, 4]
for element in array:
    print(element)

# 딕셔너리 선언 : 변수 = { 키: 값, 키: 값, ... }

# 딕셔너리 값 추가 : 딕셔너리[새로운 키] = 값

# 딕셔너리 값 제거 : del 딕셔너리[키]

# 딕셔너리 내부 키 존재 여부 : in 키워드

# for 반복문 : 딕셔너리와 함께 사용 (예: for 키 변수 in 딕셔너리)

# 함수 기분 : def 함수 이름 (매개변수, ..., sep=' ', *가변 매개변수):



# 날짜/시간과 관련된 기능 import
import datetime

now = datetime.datetime.now()
print(now.year)

#number = input("정수 입력 >")
number = '1'
if number == '1' \
    or number == '2' \
    or number == '3':
    print('if 문 참입니다!')





a = 'test'
print(a)
if True:
    print('TEST')
a = 1
print(a)

print(reversed("avc"))


