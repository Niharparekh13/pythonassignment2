from base import assignment
# from ast import Num


class fibonaaci_number(assignment):
    def run(self):
        if self <= 0:
            print("Incorrect input")
        elif self == 1:
            return 0
        elif self == 2:
            return 1
        else:
            return fibonaaci_number.run(self-1)+fibonaaci_number.run(self-2)


num = int(input("enter the value:"))
print(fibonaaci_number.run(num))
