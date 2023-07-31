a = 0
b = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num < 0:
        continue
    if num % 2 == 1:
        a += num
        b += 1

average = a/b if b > 0 else 0
print("홀수의 합=", a)
print("홀수의 평균=", average)
