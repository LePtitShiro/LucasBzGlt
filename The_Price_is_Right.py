from random import randint

start = str(input("Do you want to start the game : (YES or NO) "))

if start != 'YES': #If u don't want play
    print('Bye !')

else: #If u want play 
    print('Good luck ! :D')

    mystery_number = randint(0, 1000000) #generate a random number

    print("-"*50) #To separate the steps
    number = int(input('Enter your number (without space): ')) #Ask what numbers

    while number !=mystery_number:
      
        if number < mystery_number: # if number is smaller than mystery number
            print("-"*50)
            print("It's bigger")
            
        elif number > mystery_number: # if number is greater than mystery number
            print("-"*50)
            print("It's smaller")

        number = int(input('Enter your number (without space): ')) #Ask again what numbers
        
    print("-"*50)
    print("Well play, it's a good answer ! ") #We exit the loop if the number is equal to the mystery number
