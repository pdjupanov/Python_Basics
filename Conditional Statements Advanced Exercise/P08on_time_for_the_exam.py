
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())


exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute


if arrival_time > exam_time:
    print("Late")

    difference = arrival_time - exam_time
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif exam_time - arrival_time <= 30:
    print("On time")
    # Изчисляване на времето преди началото в минути
    difference = exam_time - arrival_time
    if difference > 0:
        print(f"{difference} minutes before the start")
elif exam_time - arrival_time > 30:
    print("Early")

    difference = exam_time - arrival_time
    if difference < 60:
        print(f"{difference} minutes before the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours before the start")
