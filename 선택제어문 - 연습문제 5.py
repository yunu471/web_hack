a, b = map(int, input('주사위를 던진 결과를 입력하세요.').strip().split())

if a >= 4 and b >= 4:
    print('이겼습니다')
elif a < 4 and b < 4:
    print('졌습니다')
else:
    print('비겼습니다')
