# Only give back the ints(Integers) from the given list
things = [1, 'bread', 4.54, 0, 'catipillar', 5, '$', 10, ':']

ints = []
others = []
for thing in things:
    if type(thing) == int:
        ints.append(thing)
    else:
        others.append(thing)

print('The ints in the list are: ', ints)
print ('The other things: ', others)
