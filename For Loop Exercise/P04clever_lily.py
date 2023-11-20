
lilly_age = int(input())
price_washing_machine = float(input())
price_for_one_toy = int(input())

saved_money = 0
birthdays_money = 0

for year in range(1, lilly_age +1):
    if year % 2 == 0:
        birthdays_money += 10
        saved_money += birthdays_money -1
    else:
        saved_money += price_for_one_toy

if saved_money >= price_washing_machine:
    remaining_money = saved_money - price_washing_machine
    print(f"Yes! {remaining_money:.2f}")
else:
    needed_money = price_washing_machine - saved_money
    print(f"No! {needed_money:.2f}")