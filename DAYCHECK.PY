def main():  # defining the main function
    week_here() # calling user function

def week_here():  # defining the user function
                  # user input below
        number = int(input("Enter a number between 1 and 7: "))
        match number:  # checking...
            case 1:
                print("Sunday")  #  If number is 1, print Sunday
            case 2:
                print("Monday")  #  If number is 2, print Monday
            case 3:
                print("Tuesday")  # If number is 3, print Tuesday
            case 4:
                print("Wednesday")  # If number is 4,Print Wednesday
            case 5:
                print("Thrusday")   # If number is 5, print Thrusday
            case 6:
                print("Friday")    # If number is 6 , print Friday 
            case 7:
                print("Saturday")  # If number is 7 , print Saturday
            case _:
                print("Invalid input")   # If number beyond this number , print Invalid input
main()


