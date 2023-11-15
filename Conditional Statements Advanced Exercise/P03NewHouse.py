type_flower = input()
number_flowers = int(input())
budget = int(input())

price_per_flower = 0


if type_flower == 'Roses':
    price_per_flower = 5
    if number_flowers > 80:
       price_per_flower = price_per_flower * 0.9

elif type_flower == 'Dahlias':
    price_per_flower = 3.80
    if number_flowers > 90:
        price_per_flower = price_per_flower * 0.85

elif type_flower == 'Tulips':
    price_per_flower = 2.80
    if number_flowers > 80:
        price_per_flower = price_per_flower * 0.85

elif type_flower == 'Narcissus':
    price_per_flower = 3
    if number_flowers < 120:
        price_per_flower = price_per_flower * 1.15

elif type_flower == 'Gladiolus':
    price_per_flower = 2.50
    if number_flowers < 80:
        price_per_flower = price_per_flower * 1.20

price = price_per_flower * number_flowers
diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {diff:.2f} leva left.")

else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
