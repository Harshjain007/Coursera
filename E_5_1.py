
num = 0
tot = 0.0
while True:
    sval = input('Enter a value:')
    if sval == 'done':
        break
    try :
        fval = float(sval)
    except :
        print('Enter valid value.')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print(tot, num, tot/num)
