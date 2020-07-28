maxNumber = int(input('Enter the number'))
oddNumbers = []

for num in range(0,maxNumber):
    if num%2 != 0:
        oddNumbers.append(num)

print('Odd numbers : ', oddNumbers)