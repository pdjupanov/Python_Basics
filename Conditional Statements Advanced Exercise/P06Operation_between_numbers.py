
number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0

if number_2 == 0:
    print(f"Cannot divide {number_1} by zero")
elif operator == '+':
   result = number_1 + number_2
   if result % 2 == 0:
       print(f"{number_1} {operator} {number_2} = {result} - even")
   else:
       print(f"{number_1} {operator} {number_2} = {result} - odd")

elif operator == '-':
   result = number_1 - number_2
   if result % 2 == 0:
       print(f"{number_1} {operator} {number_2} = {result} - even")
   else:
       print(f"{number_1} {operator} {number_2} = {result} - odd")

elif operator == '*':
   result = number_1 * number_2
   if result % 2 == 0:
       print(f"{number_1} {operator} {number_2} = {result} - even")
   else:
       print(f"{number_1} {operator} {number_2} = {result} - odd")

elif operator == '/':
    result = number_1 / number_2
    print(f'{number_1} / {number_2} = {result:.2f}')

elif operator == '%':
    result = number_1 % number_2
    print(f'{number_1} % {number_2} = {result}')
