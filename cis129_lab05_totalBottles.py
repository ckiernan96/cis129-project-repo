totalBottles = 0
counter = 0
todayBottles = 0
totalPayout = 0
y = 'keepGoing'

while True:
    counter = counter + 1 #counter for days of week
    print('Enter number of bottles returned for day #', (counter), ':')
    todayBottles = int(input()) 
    totalBottles = totalBottles + todayBottles
    if counter < 7:
        continue
    totalPayout = totalBottles / 10 #code for getting total payout

    print('The total number of Bottles collected is', totalBottles)
    print('The total paid out is $', totalPayout)
    print()
    print("Do you want to enter another week's worth of data?")
    keepGoing = input('Enter y or n:')
    if keepGoing == 'y': #resets all counters and repeats loop
        counter = 0
        totalBottles = 0
        totalPayout = 0
        continue
    else: #breaks loop if anything besides y is input
        break
print('Thank you!')
