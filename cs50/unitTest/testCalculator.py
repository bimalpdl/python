import calculator as calc 

def main():
    testCalculator()

def testCalculator():
    if calc.square(2) != 4:
        print("2 squared was not 4!")
    if calc.square(3) != 9:
        print("3 squared was not 9!")
    if calc.square(4) != 16:
        print("4 squared was not 16!")



# Python’s assert command allows us to tell the compiler that something, some assertion, is true.
# If false, it will raise AssertionError,
    assert calc.square(5) == 25  
    assert calc.square(6) == 36 



   # we can use exception handling to deal with AsssertionError.
    try:
        assert calc.square(7) == 40    # produces assertion error
    except AssertionError:
        print("7 squared was not 49!")
    try:
        assert calc.square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()
