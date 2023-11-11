#office working time 10-18 monday - saturday

hour = int(input())
day = input()

if 10 <= hour <= 18 and day != 'Sunday':
    print('open')
else:
    print('closed')
