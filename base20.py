for i in range(10):
    if i == 3:
        break
    print(i)
else:
    print('処理終了')

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('while終了')