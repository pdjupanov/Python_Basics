

while True:

    destination = input()

    if destination == "End":
        break

    budget = float(input())

    savings = 0

    while savings < budget:
        saving_amount = float(input())
        savings += saving_amount

    print("Going to {}!".format(destination))

