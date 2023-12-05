
min_number = 0

while True:
    user_input = input()

    if user_input == "Stop":
        break

    current_number = int(user_input)
    min_number = min(min_number, current_number)

print(min_number)