import sys

opened_tabs = int(input())
salary = int(input())

penalty = 0

for site in range(opened_tabs):
    site_name = input()

    if site_name == "Facebook":
        penalty = 150
        salary -= penalty
    elif site_name == "Instagram":
        penalty = 100
        salary -= penalty
    elif site_name == "Reddit":
        fine = 50
        salary -= penalty

    if salary <= 0:
        print("You have lost your salary.")
        break

print(salary)


