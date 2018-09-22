# vendor 1
class Abc:
    def fun(self):
        print('fun')

    def somefunc(self):
        print('Some func of abc')

# vendor 2
class Xyz:
    def foo(self):
        print('foo')

    def somefunc(self):
        print('Some func of xyz')

# end goal
# foo -> Xyz
# fun -> Abc
# somefunc -> Abc
class Pqr(Abc, Xyz): # MRO (method resolution order)
    # multiple inheritance
    # one child class has two parent classes
    pass

p = Pqr()

p.somefunc()
p.fun()
p.foo()
