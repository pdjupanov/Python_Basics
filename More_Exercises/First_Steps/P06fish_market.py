price_mackerel = float(input())
price_sprat = float(input())
kg_bonito = float(input())
kg_saffron = float(input())
kg_mussels = int(input())

price_bonito = price_mackerel + price_mackerel * 0.6
price_saffron = price_sprat + price_sprat * 0.8
price_mussels = 7.50

total_cost = kg_bonito * price_bonito + kg_saffron * price_saffron + kg_mussels * price_mussels


print(f'{total_cost:.2f}')