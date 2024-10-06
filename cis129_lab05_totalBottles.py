totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
y = 'keepGoing'

while True:
    totalBottles = input('Enter Total Amount of Bottles:')
    
    totalPayout = input('Enter the Total Payout:')
    
    print('Total Bottles:', totalBottles, '&', 'Total Payout', totalPayout)
        
    print("Do you want to enter another week's worth of data?")
    input('Enter y or n:')
    
