# try: 
#     num1 = int(input('Number_'))
#     num2 = int(input('Number_'))
#     print("Quotionet: " + str(num1/num2))
# except ZeroDivisionError:
#     print('0 can not be the divisior')
# except ValueError:
#     print("Please Enter Number")
# except:
#     print("Something Went Wrong.")
    
    
    
class ZeroCubeError(Exception):
    '''O can\'t be passed as a cube'''    
    
class Cube():
    def __init__(self, num):
        num = int(num)
        if num != 0:
            self.qub = num**3
        else:
            raise ZeroCubeError
        
        
        
try: 
    num = int(input('Number_'))
    num = int(input('Number_'))
except ZeroCubeError:
    print(ZeroCubeError.__doc__)
except:
    print("Something went wrong.")
else:
    print("Cube: " + str(num.qub))
finally:
    print("Execution Complete")
    

# def Cube(number):
#     '''This function cubes numbers
#        Code : print(number***3)'''
#     print(number**3)

# print(help(Cube))



    
