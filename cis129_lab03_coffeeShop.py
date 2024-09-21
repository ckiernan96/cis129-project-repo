#cis129_lab03_coffeeShop.py
print('***************************************\
     \nMy Coffee and Muffin Shop')

#Coffee Amount = value1
value1 = int(input('Number of coffees bought?'))

#Muffin Amount = value2
value2 = int(input('Number of muffins bought?'))

print('***************************************')
print('***************************************\
     \nMy Coffee and Muffin Shop Receipt')

#total muffin cost = value3
value3 = float(value1 * 5.00)
print(value1, 'Coffee at $5 each:', '$', (format(value3, '.2f'))) 

#total muffin cost = value4
value4 = float(value2 * 4.00)
print(value2, 'Muffins at $4 each:', '$',(format(value4, '.2f')))

#tax total = value5
value5 = (value3 + value4) * 0.06
print('6% tax:', value5)

print('---------')
print('Total:', (value3 + value4 + value5))
print('***************************************')
