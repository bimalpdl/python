def main():
    size = int(input("Enter the size: "))
    printSquare(size)

def printSquare(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")

        print()

main()
