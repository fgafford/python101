# Find the duplicates
numbers = [1, 2, 4, 7, 1, 5, 8, 10, 4]
print('The numbers are: ', numbers)

unique = []
for number in numbers:
        if number in unique:
            print( number, 'is in here more then once')
        else:
            unique.append(number)

print('end')
