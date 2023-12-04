total_amount = 0

while True:
    input_value = input()

    if input_value == "NoMoreMoney":
        break

    amount = float(input_value)

    if amount < 0:
        print("Invalid operation!")
        break

    total_amount += amount
    print(f"Increase: {amount:.2f}")

print(f"Total: {total_amount:.2f}")
