import random
number_to_guess = random.randint(1,1000)
guess = -1
resign = False
while guess != number_to_guess :
    instruction = input("Enter a number between 1 and 1000 {q: quitter}.) ")
    
    if not instruction.isnumeric():
        if instruction == 'q':
            resign = True
            break
        else :
            print("Instruction is invalid !")
            continue
    
    guess = int(instruction)
    if guess < number_to_guess :
        print("It's more")
    else :
        print("It's less")
if resign:
    print(f"Dommage le nombre était {number_to_guess}.")
else :
    print("Good job, you have found the number.")
