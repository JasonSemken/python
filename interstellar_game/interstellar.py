
# Requests name from user
name=input("What is your name?\n")

# Prints fuel to terminal
def fuelGuage(fuelRemaining):
    print("You have "+str(fuelRemaining)+" litres of fuel left!")

# Requests starting fuel from user
def fuelInput():
    fuelChoice=input("How much fuel do we have?\n")
    return fuelChoice

# Requests user for fuel level input and outputs standard response
def fuelRequired(fuel):
    print("We need "+str(fuel)+" litres of fuel to get there.")
    return

# Collects users fuel input and calculates fuel requirement for planet travel
def calculateFuel(fuel):
    fuelRequired(fuel)
    if int(fuelInput()) >= fuel:
        print("Let's Go!!")
    else:
        print("Shit dawg, We can't make it!!")



def planetInput():
    planetChoice=input("Where would you like to go, "+name+"?\n")

    match planetChoice:
        case "Mercury" | "mercury":
            calculateFuel(200)
        case "Venus" | "venus":
            calculateFuel(100)
        case "Earth" | "earth":
            print("Earth? We are already there "+name+".")
            planetInput()
        case "Mars" | "mars":
            calculateFuel(130)
        case "Jupiter" | "jupiter":
            calculateFuel(500)
        case "Saturn" | "saturn":
            calculateFuel(700)
        case "Neptune" | "neptune":
            calculateFuel(1000)
        case "Pluto" | "pluto":
            print("Pluto is not a planet anymore.")
            planetInput()
        case _:
            print("That isn't a planet, try again.")
            planetInput()



planetInput()