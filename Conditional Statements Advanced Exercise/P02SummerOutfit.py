
temperature = int(input())
day_time = input()

if day_time == 'Morning':
    if temperature <= 18:
        print(f"It's {temperature} degrees, get your Sweatshirt and Sneakers.")
    elif temperature <= 24:
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
    else:
        print(f"It's {temperature} degrees, get your T-Shirt and Sandals.")

elif day_time == 'Afternoon':
    if temperature <= 18:
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
    elif temperature <= 24:
        print(f"It's {temperature} degrees, get your T-Shirt and Sandals.")
    else:
        print(f"It's {temperature} degrees, get your Swim Suit and Barefoot.")

if day_time == 'Evening':
    if temperature <= 18:
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
    elif temperature <= 24:
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")
    else:
        print(f"It's {temperature} degrees, get your Shirt and Moccasins.")