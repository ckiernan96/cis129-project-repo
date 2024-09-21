#cis129_lab03_coffeeShop.py
print('* * * * * * * * * * * * * * * * * * * * * * *\
     \n     -Rainforest Breakfast Shop-')
print()
#Coffee Amount = value1
value1 = int(input('Number of coffees bought?'))
print()
#Muffin Amount = value2
value2 = int(input('Number of muffins bought?'))
print()
#Tea Amount = value3
value3 = int(input('Number of teas bought?'))
print()
#Sandwich Amount = value4
value4 = int(input('Number of sandwiches bought?'))
print()
print('* ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *')
print('* ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *')
print()
print('    Rainforest Breakfast Shop Receipt:')
print()
#total muffin cost = value5
value5 = float(value1 * 5.00)
print(value1, 'Coffee at $5 each:', '$', (format(value5, '.2f'))) 
print()
#total muffin cost = value6
value6 = float(value2 * 4.00)
print(value2, 'Muffins at $4 each:', '$',(format(value6, '.2f')))
print()
#total tea cost = value7
value7 = float(value3 * 3.00)
print(value3, 'Teas at $3 each:', '$',(format(value7, '.2f')))
print()
#total sandwich cost = value8
value8 = float(value4 * 6.00)
print(value4, 'Sandwiches at $6 each:', '$',(format(value8, '.2f')))
print()
print()
#tax total = value9
value9 = (value5 + value6 + value7 + value8) * 0.06
print('6% tax:', (format(value9, '.2f')))
print()
print('---------')
print('Total:', format(value5 + value6 + value7 + value8 + value9, '.2f'))
print()
print('* * * * * * * * * * * * * * * * * * * * * * *')
print()
print('        Have a wonderful day!')
print()
print()
print('Please leave us a good review on Yelp!\
     \nIt really helps out the business')
print()
input('Press ENTER to exit')
