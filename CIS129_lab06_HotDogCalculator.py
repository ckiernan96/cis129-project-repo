#Christopher Kiernan - CIS129
#This program is designed after a pseudocode provided to me for Lab 6. It inputs the minimum amount of hot dog and hot dog buns
# needed for the cookout along with how many of each are left over
import math
def Main():
    # Gets the Amount of People attending and how many Hot Dogs per person
    def getTotalHotDogs():
        people = input('Enter the number of people attending the cookout: ')
        hotDogs = input('Enter the number of Hot Dogs for each person: ')
        return(int(people) * int(hotDogs))
    total = getTotalHotDogs()

    DOGS = 10 # Constant of Hot Dogs in Package
    BUNS = 8  # Constant of Hot Dog Buns in Package 

    # Variables
    dogsLeft = int(10 - int(total) % 10) % 10
    bunsLeft = int(8 - int(total) % 8) % 8
    minDogs = math.ceil(int(total) / 10)
    minBuns = math.ceil(int(total) / 8)

    # Shows Results from previous functions
    print('Minimum packages of hot dogs needed: ', minDogs)
    print('Minimum packages of hot dog buns needed: ', minBuns)
    print('Hot dogs left over: ', dogsLeft)
    print('Hot dog buns left over:', bunsLeft)

Main()
input('Press Enter to Exit')
