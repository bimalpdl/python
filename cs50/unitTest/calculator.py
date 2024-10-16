def main():
    x = int(input("What is the value of x?: "))
    print("Square of {} is {}.".format(x,square(x)))

def square(num):
    return num * num

if __name__ == "__main__":
    main()
