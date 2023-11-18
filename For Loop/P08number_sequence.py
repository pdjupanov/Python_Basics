
input_number = int(input())

max_number = min_number = int(input())

for _ in range(input_number-1):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
