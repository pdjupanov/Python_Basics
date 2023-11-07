# decor = 10% from the budget
# if statist are more than 150 10% discount from clothing

budget = float(input())
statist = int(input())
# for one statist
price_for_clothing = float(input())

decor = budget * 0.10
price_for_clothing = price_for_clothing * statist

if statist > 150 :
    price_for_clothing = price_for_clothing - (price_for_clothing * 0.10)

expenses =  price_for_clothing + decor
diff = abs ( budget - expenses )

if budget >= expenses:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
 print("Not enough money!")
 print(f"Wingard needs {diff:.2f} leva more.")



