input_number = int(input())

left_sum = 0
right_sum = 0

for _ in range(input_number):
    number = int(input())
    left_sum += number

for _ in range(input_number):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")