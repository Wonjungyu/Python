
# 출력문      

print("hello anan")

# 반복문
#x 가 0부터 8까지 순서대로 출력

for x in range(9) :
	print(x, x**2)
	
print()  #=============================N E X T=============================

#입력문

asd = input ('이름을 입력하시오 : ')

#변수

my = 'hello python'
print(my)
print()
print(asd)

# 줄 뛰어넘기
print()  #=============================N E X T=============================

var1 ='파이썬 객체지향 이야기'
var2 ='파이썬 객체지향 이야기'

# 객체 비교하기
print(var1 is var2) #" False"

# 변수의 데이터 값 비교하기
print(var1 == var2) #" True "

print()  #=============================N E X T=============================


#객체 식별자 확인
print(id(var1)) #"5661760"
print(id(var2)) #"5661805"

print()  #=============================N E X T=============================

# 데이터 변수 확인
print(type(var1)) #" <claa 'str'>"


print()  #=============================N E X T=============================

#특정 표기법 변경
print(var1.replace('파이썬' , 'Python'))
print(var1)


print()  #=============================N E X T=============================
