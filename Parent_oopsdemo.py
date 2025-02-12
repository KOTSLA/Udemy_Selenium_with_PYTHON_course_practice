#parent class

class Calculator:
    num = 100       #class variables

    #default constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")


    @staticmethod               #pycharm give this error fix
    def getdata():
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)  #syntax to create objects in python
obj.getdata()  #to get method from class
print(obj.summation())               #to get value from class

obj1 = Calculator(4, 5)  #syntax to create any objects in python
obj1.getdata()           #to get method from class
print(obj1.num)               #to get value from class
print(obj1.summation())
