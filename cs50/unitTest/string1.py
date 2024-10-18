def main():
    name = input("Enter your name: ")
    print(hello(name))

def hello(naam = "Duniya"):
    return f"Hello, {naam}"

if __name__ == "__main__":
    main()
