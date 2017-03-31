my_intput = input('Please input your age: ')
age = int(my_intput)

if age >= 6 and age < 18:
    print('Teenager')
elif age >= 18:
    print('Adult')
else:
    print('Kid')


# Test
height = 1.75
weight = 80.5

bmi = weight / (height**2)
print('BMI = %.2f' % bmi)

if bmi > 32:
    print('严重肥胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')
