# List overlap
listA = [1,1,2,3,5,8,13,21,34,55,89]
listB = [1,2,3,7,9,13,14,55,67,98,101,30]

# ???
matches = []
for i in range(len(listA)):
    if (listA[i] in listB) and (listA[i] not in matches):
        matches.append(listA[i])


print('The matches are: ', matches)
# Example output:
#       [1,2,3,13,55]
