class Student_second():
    __studentid = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__studentid is None:
            cls.__studentid = super().__new__(cls)
        return cls.__studentid
    
    def __init__(self, name, age):
        self.name = name
        self.age = age   
    
    def say_hello(self):
        print("Student", self.name, "says hello")


def first_variant(cls):
    d = {}
    def singleton(*args, **kwargs):
        if cls not in d:
            d[cls] = cls(*args, **kwargs)
        return d[cls]
    return singleton

@first_variant
class Student_first:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print("Student", self.name, "says hello")


if __name__ == "__main__":

    print("First variant: ")

    a1 = Student_first("Mike", 28)
    b1 = Student_first("Mira", 21)
    
    print(a1)
    print(b1)
    print(a1 is b1)


    print("Second variant: ")

    a2 = Student_second("Ann", 19)
    b2 = Student_second("Den", 25)
    
    print(a2)
    print(b2)
    print(a2 is b2)

