import math
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_1m = float(input())

time = distance_in_meters * time_in_seconds_1m
delay_distance = distance_in_meters / 15.0
delay_time = math.floor(delay_distance) * 12.5

time = time + delay_time

if time >= record_in_seconds:
    time = time - record_in_seconds
    print(f'No, he failed! He was {time:.2f} seconds slower.')

elif time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
