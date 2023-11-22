price_vegetables_kg = float(input())
price_fruit_kg = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

vegetables_price = price_vegetables_kg * vegetable_kg
fruit_price = fruit_kg * price_fruit_kg

final_price = (vegetables_price + fruit_price) / 1.94

print(f'{final_price:.2f}')