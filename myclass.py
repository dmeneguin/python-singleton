from singleton_metaclass import SingletonMetaClass

class MyClass(metaclass=SingletonMetaClass):
    def __init__(self):
        self.name = 'abc'
        