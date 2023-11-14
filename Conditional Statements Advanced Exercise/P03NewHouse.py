
flower = input()
quantity_of_flowers = int(input())
budget = int(input())

# rose = 5  dahlia = 3.80   tulip = 2.80  narciss = 3    gladiolus = 2.50

price = 0
discount = 0

if flower == 'Roses':
    price = 5 * quantity_of_flowers
    if quantity_of_flowers > 80:
        discount = 0.10

elif flower == 'Dahlias':
    price = 3.80 * quantity_of_flowers
    if quantity_of_flowers > 90:
        discount = 0.15

elif flower == 'Tulips':
    price = 2.80 * quantity_of_flowers
    if quantity_of_flowers > 80:
        discount = 0.15

# the two nxt if statements discount = increase price

elif flower == 'Narcissus':
    price = 3 * quantity_of_flowers
    if quantity_of_flowers < 120:
        discount = 0.15
        price = price + discount

elif flower == '"Gladiolus':
    price = 3 * quantity_of_flowers
    if quantity_of_flowers < 80:
        discount = 0.20
        price = price + discount


diff = price - budget

price = quantity_of_flowers * (price - discount)

print()


