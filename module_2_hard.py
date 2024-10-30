n = int(input('Enter the number: '))
while n < 3 or n > 20:
    n = int(input('Enter the number: '))
password = ''

for i in range(1, 20):
    for j in range(i, 20):
        if n % (i + j) == 0 and not (i == j):
            password += str(i)
            password += str(j)

print(f'{n} - {password}')
