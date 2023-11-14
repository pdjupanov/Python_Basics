
import  sys
city = input()
sales = float(input())

commission = 0
if city == 'Sofia':
    if sales <= 500:
        commission = 0.05
    elif sales <= 1000:
        commission = 0.07
    elif sales <=10000:
        commission = 0.08
    else:
        commission = 0.12

elif city == 'Varna':
    if sales <= 500:
        commission = 0.045
    elif sales <= 1000:
        commission = 0.075
    elif sales <=10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13
    else:
        print('error')

elif city == 'Plovdiv':
    if sales <= 500:
        commission = 0.055
    elif sales <= 1000:
        commission = 0.08
    elif sales <=10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
    else:
        print('error')

else:
    print('error')
    sys.exit()
commission = sales * commission


print(format(commission, '.2f'))


