class Person:
    def __init__(self,initialAge):
        if initialAge>=0:
            self.age=initialAge
        else:
            self.age=0
            print("Age is not valid, setting age to 0.")

    def yearPasses(self):
        self.age=self.age+1

    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager")
        else:
            print("You are old")


T = int(input().strip())
for i in range(T):
    temp=int(input())
    p1=Person(temp)
    p1.amIOld()
    p1.yearPasses()
    p1.yearPasses()
    p1.yearPasses()
    p1.amIOld()

    
    