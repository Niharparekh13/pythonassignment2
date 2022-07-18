from base import assignment
class armstrong_number(assignment):
  def run(self):
    sum = 0
    temp = num
    while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10
      if num == sum:
        print(num,"is an Armstrong number")
    else:
     print(num,"is not an Armstrong number")
num = int(input("Enter a number: "))
print(armstrong_number.run(num))