# Containership ----

class Coder():
    def __init__(self):
        self.name = input('Name_')
        self.lang = input("Languages_")
    def sho_details(self):
        print("Name:" + str(self.name))
        print("Languages:" + str(self.lang))
     
# class Pythoneer():
#     def __init__(self):
#         self.profile = Coder()
#     def profile(self):
#         self.profile.sho_details()
        
class Pythoneer():
    def __init__(self):
        self.coder_profile = Coder()  
    def display_profile(self):
        self.coder_profile.sho_details()
    
jake = Pythoneer()
jake.display_profile()