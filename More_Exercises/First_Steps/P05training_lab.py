width = float(input())
height = float(input())

workplace_area = 70 * 120

corridor_area = 100 * width

door_area = 160 * height
podium_area = 160 * 10 * 2

total_area_per_workplace = workplace_area + door_area + podium_area

left_workspace = int(width - corridor_area) / total_area_per_workplace
right_workplaces = left_workspace

total_workplaces = left_workspace + right_workplaces

print(total_workplaces)