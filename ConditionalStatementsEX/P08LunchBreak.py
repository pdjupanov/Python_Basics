import math

tv_series = input()
episode = int(input())
break_time = int(input())

#lunch time = 1/8 from the break
#chill time = 1/4  from break

lunch = break_time * 12.5 /100
chill = break_time * 0.25

break_time = break_time - lunch - chill

diff = math.ceil(episode - break_time)

if episode < break_time :
    print(f"You have enough time to watch {tv_series} and left with {break_time-episode:.0f} minutes free time.")

else:
    print(f"You don't have enough time to watch {tv_series}, you need {diff:.0f} more minutes.")


