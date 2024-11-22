from random import shuffle

while True:
    inputStudentName = str(input("Enter You Name: "))
    
    # Check if the user wants to exit
    if inputStudentName.upper() == "EXIT":
        print("Goodbye!")
        exit()
    else:
        listGift = ["Pen", "Pencil", "ColorBox", "CompassBox", "EraserBox"]
        shuffle(listGift)
        listGift1 = ["LaptopBag", "SportsBag", "Bag", "HandBag", "Shoes"]
        shuffle(listGift1)
        listGift2 = ["Book", "Copy", "Notebook", "PencilBox", "PenBox"]
        shuffle(listGift2)

        print("\n" + "- " * 6)
        
        print("[:)] Hello " + inputStudentName + "!")
        print(f"[:)] 1. Gift Name: {listGift[0]}")
        print(f"[:)] 2. Gift Name: {listGift1[0]}")
        print(f"[:)] 3. Gift Name: {listGift2[0]}")
        print("Thank you for using the gift generator!")
        print("- " * 6)
        # Continue the loop
