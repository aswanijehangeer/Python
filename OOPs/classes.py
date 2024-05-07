# Creating our own class
# Class Methods
 
class Coder():
    def __init__(self, name):
        self.Name = name
    def info(self):
        print(self.Name)
    def is_pythonner(self):
        if "Python" in self.language:
            print("TRUE")
        else:
            print("FALSE")


cd = Coder("Jehangeer")
cd.language = ["Rust", "Python"]

# cd.is_pythonner()

del(cd.language)

# print(cd.language)



## Class artibutes and Naming conventions

class Python():
    name = 10
    _age = 18
    __key = 89
    def __init__(self):
        pass
    def python_code(self):
        print("Coding")

py = Python()
# py.python_code()



## Functions vs Class Methods

class Coder():
    def __init__(self, name):
        self.name = name
    def get_lang(self, lang):
        self.lang = lang

def is_pythonner(lst):
    if 'Python' in lst:
        print(True)
    else:
        print(False)

cd = Coder("Saraj")
cd.get_lang(["Python", "Rust"])

# is_pythonner(cd.lang)



## Operator overloading on user-defined classes

class Algebra():
    def __init__(self, r = 0.0, i = 0.0):
        self.real = r
        self.imag = i
    def __add__(self, y):
        self.real = self.real + y.real
        self.imag = self.imag + y.imag
        return self
    def sho_val(self):
        print(self.real, self.imag)
        
num1 = Algebra(2.5, 6.35)
num2 = Algebra(1.45, 3.35)

num3 = num1 + num2
num3.sho_val()


## Built-in overloading on user-defined classes

class Numeric_Str():
    def __init__(self, Str = ""):
        self.Str = Str
    def __int__(self):
        return int(self.Str)

num = Numeric_Str("1099")
pro = int(num.Str)*2
print(pro)


## Creating user-defined iterable classes

class SumPair():
    def __init__(self, lst):
        self.List = lst
        self.List_len = len(lst)
        self.i1 = 0
        self.i2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i2 == self.List_len:
            raise StopIteration
        else:
            self.sum_pair = self.List[self.i1] + self.List[self.i2]
            self.i1 += 1
            self.i2 += 1
            return self.sum_pair
        
l = SumPair([12, 33, 56, 78, 12, 33])
# print(l.List_len)

for ele in l:
    print(ele)