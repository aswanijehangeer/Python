# class MyClass():
#     pass

# obj = MyClass()
# obj.


## Multi-level Inheritance ----

class Coder():
    def code(self):
        print("Codin")

class Pythonner(Coder):
    def py_code(self):
        print("Coding in Python!")

class Django(Pythonner):
    def web_dev(self):
        print("New HTML @ Django")
        
web = Django()
web.code()
web.py_code()
web.web_dev()


## Multiple Inheritance ----

class Coder():
    def __init__(self):
        self.name = input("Name_ ")
    
class Pythonner():
    def __init__(self):
        self.works = input("Works_ ")
    
class WebDev(Coder, Pythonner):
    def __init__(self):
        Coder.__init__(self)
        Pythonner.__init__(self)
    def start_new(self):
        print('new.html @ Django')

web = WebDev()
web.start_new()