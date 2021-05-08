while(True):
    work = input("s Square and c for cube---->")

    if work=="s":
            number = int(input("Enter a number---->"))
            square = number*number
            print(square)
            continue

    if work=="c":
            number = int(input("Enter a number---->"))
            cube = number*number*number
            print(cube)
            continue