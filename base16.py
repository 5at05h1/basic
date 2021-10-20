# if and or not

# msg = 'yellow'
# if msg == 'blue':
#     print('すすめ')
# elif msg == 'red':
#     print('止まれ')
# else:
#     print('注意')

age = 70
if age < 20:
    print('20未満')
elif age <= 40:
    print('20以上40以下')
elif age >= 60:
    print('60以上')
else:
    print('それ以外')

gender = 'woman'
age = 10
if gender == 'man' or age < 20:
    print('未成年男性')

if gender != 'man':
    print('男ではない')