
budget = float(input())
season = input()

price = 0
place = 0
if budget <= 100:
    if season == 'winter':
        price = budget * 0.70
        place = 'Hotel'
    elif season == 'summer':
        price = budget * 0.30
        place = 'Camp'
    print('Somewhere in Bulgaria')
    print(f'{place} - {price:.2f}')

elif budget <= 1000:
    if season == 'winter':
        price = budget * 0.80
        place = 'Hotel'
    elif season == 'summer':
        price = budget * 0.40
        place = 'Camp'
    print('Somewhere in Balkans')
    print(f'{place} - {price:.2f}')


else:
    if season == 'winter' or 'summer':
        price = budget * 0.90

        print('Somewhere in Europe')
        print(f'Hotel - {price:.2f}')


