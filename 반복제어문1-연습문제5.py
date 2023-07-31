sum = 0
count = 0
while True :
    num = int(input())
    if num % 2 == 1:
        sum += num
        count = count + 1
    if num == 0:
        break
avg = sum // count         
print('홀수의 합 = ' + str(sum))
print('홀수의 평균 = ' + str(avg))
