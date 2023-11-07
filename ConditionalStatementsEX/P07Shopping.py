#if videocards are bigger than proccesors have 15% discount from the final price

#videocard 250 lv
#cpu 35 % from the videocard for pcs
#ram 10% from the from the videocard pcs

budget = float(input())
gpu_quantity = int(input())
cpu_quantity = int(input())
ram_quantity = int(input())

gpu_price = gpu_quantity * 250
cpu_price = gpu_price * 0.35
ram_price = gpu_price * 0.10

total_price = gpu_price + (cpu_price*cpu_quantity + ram_price*ram_quantity)

discount = 0

if gpu_quantity > cpu_quantity:
    discount = total_price * 0.15

total_price = total_price - discount
diff = budget - total_price

if total_price <= budget :
  print(f'You have {diff:.2f} leva left!')

else:
    print(f'Not enough money! You need {total_price-budget:.2f} leva more!')