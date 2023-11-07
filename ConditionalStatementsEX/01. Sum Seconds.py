import math
timeFirst = int(input())
timeSecond = int(input())
timeThird = int(input())

totalTime = timeFirst + timeSecond + timeThird

minutes = totalTime // 60
seconds = totalTime  % 60

minutes = math.floor(minutes)

if seconds <10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
