num = int(input("Enter the number:"))

if num%3 == 0:
    print ("Fizz")
if num%5 == 0:
    print ("Buzz")
if num%3 & 5 == 0:
    print ("FizzBuzz")
else:
    print (num)

