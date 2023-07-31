n = int(input("정수를 입력하세요: "))

count = 1
total = 0

while count <= n:
    total += count
    count += 1

print("1부터 {}까지의 합은 {}입니다.".format(n, total))