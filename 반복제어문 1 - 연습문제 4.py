count = 0
total = 0

while True:
    score = int(input())
    
    if score == 0:
        break
    
    count += 1
    total += score

if count > 0:
    average = round(total / count, 2)
    print("입력된 자료의 개수 =", count)
    print("입력된 자료의 합계 =", total)
    print("입력된 자료의 평균 =", average)
else:
    print('')