class Number():
    def __init__(self):
        self.num = 0
    def increase(self):
        self.num += 1
    def decrease(self):
        self.num -= 1

class NewNumber(Number):
    number_new = 11 # public variable (globally accessed)
    _new = 12 # variable for NewNumber()
    __new = 15 # variable just inside NewNumber()
    def __init__(self):
        super().__init__()
    def sho_val(self):
        print("Value: ", str(self.num))

num = NewNumber()
num.increase()
num.increase()
# num.decrease()
num.sho_val()


