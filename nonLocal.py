def outer():
    var1 = 10
    var2 = 20
    def inner():
        nonlocal var1 
        var1 = 15     # since we've used 'nonlocal' on var1, it will update the original variable even in outer() function scope
        var2 = 25     # notice that we haven't declared var2 as nonlocal as the change will be made
        # local variable var2 inside inner() function
        print("Value of var1 = ",var1)
        print("Value of var2 = ",var2)
    inner()
    print("Value of var1 = ",var1)
    print("Value of var2 = ",var2)
outer()
