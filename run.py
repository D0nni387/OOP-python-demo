from classes.vehicle import Car, Bike

fiesta = Car("Petrol", 450)
ninja = Bike("Petrol", 200)


def driving(): 
    print(fiesta.explain())
    print(ninja.explain())

    while fiesta.range > 0:
        print(fiesta.range, "miles left!")
        action = input("how far are we going \n")

        if action.isnumeric():
            fiesta.drive(int(action))
        else:
            print("you can't drive letters!")

    print("we're out of fuel!")

driving()

