def week():
    week_here()

def week_here():
    # user input below
        number = int(input("Enter a number between 1 and 7: "))
        match number:
            case 1:
                print("Sunday")
            case 2:
                print("Monday")
            case 3:
                print("Tuesday")
            case 4:
                print("Wednesday")
            case 5:
                print("Thrusday")
            case 6:
                print("Friday")
            case 7:
                print("Saturday")
            case _:
                print("Invalid input")
week()
