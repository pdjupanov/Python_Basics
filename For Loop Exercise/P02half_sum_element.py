from math import inf

input_numbers = int(input())

sum = 0
max_number = -inf

for number in range(input_numbers):
    current_number = int(input())
    sum += current_number

    if current_number > max_number:
        max_number = current_number

if max_number == sum - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number- (sum - max_number))
    print('No')
    print(f'Diff = {diff}')