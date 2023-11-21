
number_of_groups = int(input())

musala_counter = 0
montblanc_counter = 0
kilimandjaro_counter = 0
k2_counter = 0
everest_counter = 0

all_people = 0

for _ in range(number_of_groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala_counter += people_in_group
    elif people_in_group <= 12:
        montblanc_counter += people_in_group
    elif people_in_group <= 25:
        kilimandjaro_counter += people_in_group
    elif people_in_group <= 40:
        k2_counter += people_in_group
    elif people_in_group > 40:
        everest_counter += people_in_group
    all_people += people_in_group



musala_percentage = (musala_counter / all_people) * 100
montblanc_percentage = (montblanc_counter / all_people) * 100
kilimandjaro_percentage = (kilimandjaro_counter / all_people) * 100
k2_percentage = (k2_counter / all_people) * 100
everest_percentage = (everest_counter / all_people) * 100

print(f'{musala_percentage:.2f}%')
print(f'{montblanc_percentage:.2f}%')
print(f'{kilimandjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')
