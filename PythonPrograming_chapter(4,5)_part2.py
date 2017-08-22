
sum = int('350')+350
print(sum)
print()

pocket = [4,6,1,9]

print(type(pocket))
print()
print(len(pocket))
print()

# 배열 번호가 '-'일 경우 뒷 순서대로 나타낸다. 
print(pocket[-1])
print()

pocket[0] = 5
print(pocket)
print()

# 리스트 끝에 '7'이라는 숫자는 추가한다.
pocket.append(7)
print(pocket)
print()

# 리스트 안에 있는 '1'이라는 값을 찾아 삭제한다.
pocket.remove(1)
print(pocket)
print()

# 리스트 안에 (1+1)번째의 3이라는 값을 삽입한다.
pocket.insert(1,3)
print(pocket)
print()

# 리스트 안에 (3+1)번째의 값을 제거 한후
# 배열을 순서에 맞게 다시 정리한다.
pocket.pop(3)
print(pocket)
print()

# 배열의 (1+1)부터 (3+1)까지 배열의 값을 삭제한다.
print(pocket[1:3])
print()


# 배열의 -2부터 끝까지 배열의 값을 삭제한다.
print(pocket[-2:])
print()

# 배열의 합치기 && 확장하기
a=[1,2,3]
b=[4,5,6]
c= a+b
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print()

# 객체를 새로 만들지 않고 그대로 붙여 넣고 싶을떄
a.extend(b)
print(a)
print()

# 리스트의 삭제를 위한 함수
del a[0]
print(a)
del a[1:3]
print(a)
del a[:]
print(a)





