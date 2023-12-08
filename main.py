from myclass import MyClass

m1 = MyClass()
m2 = MyClass()

if id(m1) == id(m2):
    print('equal')
else:
    print('nequal')