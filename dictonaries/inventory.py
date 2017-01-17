inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}


'''
# 1. Print out all the things the user has
Example:
gold: 500
pouch: ['xylophone', 'dagger', 'bedroll', 'bread loaf']
backpack: ['xylophone', 'dagger', 'bedroll', 'bread loaf']
'''
print('# 1')
def printInventory():
	print('=== Inventory ===')
	print('gold:',inventory['gold'])
	print('pouch:',inventory['pouch'])
	print('backpack:',inventory['backpack'])
	print('=================')

printInventory()


'''
# 2. Make an addGold fuction and increase the players gold by 250 and then print out the new inventory
Example output:
gold: 750
pouch: ['flint', 'twine', 'gemstone']
backpack: ['xylophone', 'dagger', 'bedroll', 'bread loaf']
'''
print('# 2')
def addGold(amount):
	inventory['gold'] = inventory.get('gold') + amount

addGold(250)
printInventory()


'''
# 3. Make an addToBackpack fuction and add a flute before printing out the new inventory.
Example output:
gold: 750
pouch: ['flint', 'twine', 'gemstone']
backpack: ['xylophone', 'dagger', 'bedroll', 'bread loaf','flute']
'''
print('# 3')
def addToBackpack(item):
	inventory['backpack'].append(item)

addToBackpack('flute')
printInventory()


'''
# 4. Make a removeFromBackpack function and remove the bread load from the players pack and print the new inventory
Example output:
gold: 750
pouch: ['flint', 'twine', 'gemstone']
backpack: ['xylophone', 'dagger', 'bedroll', 'flute']
'''
print('# 4')
def removeFromBackpack(item):
	inventory['backpack'].remove(item)

removeFromBackpack('bread loaf')
printInventory()

'''
Bonus:
Make a moveToBackpack function that takes an item from the pouch and moves it to the backpack.
Move the flint to the backpack and print out the inventory.
Example output:
gold: 750
pouch: ['twine', 'gemstone']
backpack: ['xylophone', 'dagger', 'bedroll', 'flute', 'flint']
'''
print('# Bonus:')
def moveToBackpack(item):
	inventory['pouch'].remove(item)
	inventory['backpack'].append(item)

moveToBackpack('flint')
printInventory()
