print("Select the Option")
print("1.Fibonaaci")
print("2.Prime Number")
print("3.Armstrong")
a = int(input("Enter the option you want:"))
if (a == 1):
  from files.fibonaaci import fibonaaci_number
  fibonaaci_number()
elif (a == 2):
  from files.prime import prime_number
  prime_number()
elif (a == 3):
  from files.armstrong import armstrong_number
  armstrong_number()
else:
    print("Invalid Number")
