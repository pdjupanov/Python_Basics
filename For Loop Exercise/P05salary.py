import sys

opened_tabs = int(input())
salary = int(input())

penalty_price = 0
remaining_salary = 0

for _ in range(opened_tabs):
    site_name = input()
    if site_name == "Facebook":
        penalty_price -= 150
    elif site_name == "Instagram":
        penalty_price -= 100
    elif site_name == "Reddit":
        penalty_price -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break


if remaining_salary > 0:
    print(remaining_salary)

