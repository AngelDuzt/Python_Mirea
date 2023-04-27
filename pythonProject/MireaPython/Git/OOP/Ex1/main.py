class Test:
    static_var1 = 3
    static_var2 = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b




obj = Test(6, 7)
print(dir(Test))
print(dir(obj))
print(vars(Test))
print(vars(obj))
print(Test.__dict__)
print(obj.__dict__)
