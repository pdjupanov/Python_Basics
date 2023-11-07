# price for jigsaw = 2.60/ doll = 3 / bear = 4.10 / minions = 8.20 / trucks = 2

# input 1 = price for holiday
price_for_holiday = float(input())

# input 2 = number_of_jigsaws
jigsaws = int(input())

# input 3 = dolls
dolls = int(input())

# input 4 = bears
bears = int(input())

# input 5  = minions
minions = int(input())

# input 6 = trucks
trucks = int(input())

# sum of the toys price
toys_price = (jigsaws * 2.60) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)

# sum of toys
toys_quantity = jigsaws + dolls + bears + minions + trucks

# check if the toys are 50 or more than discount 25%
if toys_quantity >= 50 :
  toys_price = toys_price - (toys_price * 0.25)

# from the final price the rent is 10%
toys_price = toys_price - (toys_price * 0.10)

# check the left or needed money
diff = abs(toys_price - price_for_holiday)

# output if money are enough  "Yes! {оставащите пари} lv left
if toys_price >= price_for_holiday:
    print(f'Yes! {diff:.2f} lv left.')

# output if money are not enough "Not enough money! {недостигащите пари} lv needed.
else:
    print(f'Not enough money! {diff:.2f} lv needed.')

