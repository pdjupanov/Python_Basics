
max_number = 0

while True:
    user_input = input()

    if user_input == "Stop":
        break

    current_number = int(user_input)

    if current_number > max_number:
        max_number = current_number

print(max_number)

