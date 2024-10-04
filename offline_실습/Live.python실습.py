# CPU 연산자 응용
# print(0b11011110&0b11011) #
# print(bin(0b11011110&0b11011)) # 2진수의 연산을 2진수로 확인하고 싶을때
# print(0x4A3 | 25)
# print(bin(0x4A3),bin(25))

# 비트 연산 응용
# print(1)
# print(1<<1, bin(1<<1))
# print(1<<2, bin(1<<2))
# print(1<<3, bin(1<<3))
# print(1<<4, bin(1<<4))
# print(7>>2)

# 비트 연산자 응용 1
# arr = [1,2,3,4]
# print(f'부분집합의 수: {1<<len(arr)}')
#
# for i in range(1 << len(arr)):
#     print(i,end= ' ')
# print()

# 비트연산자 응용 2
# arr = [1, 2, 3, 4]
# # i의 의미 : i번째 부분집합
# for i in range(1<<len(arr)):
#     for idx in range(len(arr)):
#         # i & (1<<idx)
#         # -i번째 부분집합에 idx요소가 포함되어 있나요 ?
#         if i&(1<<idx):
#             print(arr[idx],end=' ')
#     print()

# print(bin(4))
# print(bin(~4))
# print(~4)

# 실수 연산
t = 0.1
print(f'{t:.20f}')

# 비트로 표현하면 무한반복되는 숫자끼리 더하기 때문에
# 허용범위 안이면 T 밖이면 F
print(0.1+0.1 == 0.2) # True
print(0.1+0.1+0.1 == 0.3) # False
