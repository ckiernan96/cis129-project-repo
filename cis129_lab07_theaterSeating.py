def main():    
    # displays the welcome text, seats per section, and the cost of each seat
    displayWelcome()
    
    # Variables
    seatsA = 0
    seatsB = 0
    seatsC = 0
    subA = 0
    subB = 0
    subC = 0
    # call to inputTotal
    inputTotal(seatsA, seatsB, seatsC, subA, subB, subC)
    # Constants
    A = 300
    B = 500
    C = 200
    costA = 20
    costB = 15
    costC = 10

def displayWelcome():
    print("Welcome to the theater!")
    print()

    # function text
    print(f"There are {A} seats in Section A. Each seat costs ${costA}.")
    print()
    print(f"There are {B} seats in Section B. Each seat costs ${costB}.")
    print()
    print(f"There are {C} seats in Section C. Each seat costs ${costC}.")
    print()
    return displayWelcome

# inputs to show how many seats were sold in each section
def inputTotal(seatsA, seatsB, seatsC, subA, subB, subC):
    # Section A inputs
    seatsA = int(input("How many seats were sold in Section A?"))
    subA = int(seatsA * costA)
    print(f"There were {seatsA} seats sold in Section A.")
    print(f"The current subtotal for all seats is ${subA}")
    print()
    
    # Section B inputs
    seatsB = int(input("How many seats were sold in Section B?"))
    subB = int(seatsB * costB)
    print(f"There were {seatsB} seats sold in Section B.")
    print(f"The current subtotal for all seats is ${subA + subB}")
    print()
    
    # Section C inputs
    seatsC = int(input("How many seats were sold in Section C?"))
    subC = int(seatsC * costC)
    print(f"There were {seatsC} seats sold in Section C.")
    print(f"The current subtotal for all seats is ${subA + subB + subC}")
    print()
    
    print(f"There were a total of {seatsA} many seats sold in Section A and the subtotal for Section A is ${subA}.")
    print()
    print(f"There were a total of {seatsB} many seats sold in Section A and the subtotal for Section B is ${subB}.")
    print()
    print(f"There were a total of {seatsC} many seats sold in Section A and the subtotal for Section C is ${subC}.")
    print()
    print(f"The total number of seats sold is {seatsA + seatsB + seatsC} and the total money earned is ${subA + subB + subC}.")
    return seatsA, seatsB, seatsC, subA, subB, subC
        
# calls main
main()
input("Press Enter to Exit")
