# r rows    c collum

#priemere = 12
#normal = 7.50
#discount = 5

type_projection = input()
rows = int(input())
column = int(input())

price = 0

if type_projection == 'Premiere':
    price = (rows * column) * 12

elif type_projection == 'Normal':
    price = (rows * column) * 7.50

elif type_projection == 'Discount':
    price = (rows * column) * 5

print(f'{price:.2f} leva')
