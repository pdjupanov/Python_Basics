
budget_of_the_group = int(input())
season = input()
number_of_fisherman = int(input())

rent = 0
additional_discount = 1.0

if season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Spring':
    rent = 3000
elif season == 'Winter':
    rent = 2600

if number_of_fisherman <= 6:
    rent = rent * 0.9
elif number_of_fisherman <=11:
    rent = rent * 0.85
else:
    rent = rent * 0.75

if season != 'Autumn' and number_of_fisherman % 2 == 0:
    rent = rent * 0.95

if budget_of_the_group >= rent:
    print(f'Yes! You have {budget_of_the_group - rent:.2f} leva left.')
else:
    print(f'Not enough money! You need {rent - budget_of_the_group:.2f} leva.')





