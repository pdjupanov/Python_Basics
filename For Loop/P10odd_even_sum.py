input_numbers = int(input())

odd_sum = 0
even_sum = 0

for index in range(0, input_numbers):
    number = int(input())
    if index % 2 == 0:
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number

difference = abs(even_sum-odd_sum)

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {difference}')
