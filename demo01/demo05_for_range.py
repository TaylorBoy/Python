# for loop. range
sum = 0

for x in range(101):
    sum += x
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s!' % name)
print('\n')

n = 0

while n <= len(L) - 1:
    print('Hello, %s!' % L[n])
    n += 1
