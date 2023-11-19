# int range 1 - 1000
# p1 range < 200
# p2 range < 399
# p3 range < 599
# p4 range < 799
# p5 range > 800
# input number of iterations
# var to store number
# if statement for the percentage + counter for the numbers in each if statement


input_numbers = int (input()) # range 1 - 1000

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0

for number in range(input_numbers):
    current_number = int(input())
    if current_number < 200:
        p1_counter += 1
    elif current_number <= 399:
        p2_counter += 1
    elif current_number <= 599:
        p3_counter += 1
    elif current_number <= 799:
        p4_counter += 1
    elif current_number >= 800:
        p5_counter += 1

p1_percentage = (p1_counter / input_numbers) * 100
p2_percentage = (p2_counter / input_numbers) * 100
p3_percentage = (p3_counter / input_numbers) * 100
p4_percentage = (p4_counter / input_numbers) * 100
p5_percentage = (p5_counter / input_numbers) * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')
