def abc():
    # local to the function
    a = 9 # scope is abc()
    def pqr(): # scope is abc()
        print(a) # this will work
        # inner function can access the enclosing function variables
        # closures

    print(a)
    print(pqr)

    pqr()

abc()
# print(a) # will not work
# pqr() # will not work
