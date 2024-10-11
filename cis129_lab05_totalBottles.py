#Christopher Kiernan
#10/10/2024
#This code totals the amount of bottles collected during a week and calculates the total payout from them.
#It will continue to loop as long as the input from the user during the final prompt is y.

#Sets all values to 0 before entering the loop
totalBottles = 0
counter = 0
todayBottles = 0
totalPayout = 0
y = 'keepGoing'

#Main loop of program
while True:
#Calculates the number of bottles collected during the days of the week
    counter = counter + 1 #counter for days of week
    print('Enter number of bottles returned for day #', (counter), ':')
    todayBottles = int(input()) 
    totalBottles = totalBottles + todayBottles
    if counter < 7:
        continue

#After inputing all information, this code reads off the information and totals both the bottles and payout of the input data
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
