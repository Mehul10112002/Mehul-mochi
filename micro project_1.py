print("~~~~micro project~~~~")

num1 = float(input("enter  first number: "))
num2 = float(input("enter  second number here: "))
print("press 1for addition \npress 2 for subtraction \npress 3 for multification \npress 4 for division")
print(round(num1))
print(round(num2))
while True:
   choice =int(input("enter your choice  form1-4 :"))
   if choice == 1:
     print ("The addition of given two number is",num1 + num2)
   elif choice == 2:
     print ("The substraction of given two number is",num1 -  num2)
   elif choice == 3:
     print ("The multiplication of given two number is",num1 * num2)
   elif choice ==4:
     print ("The division of given two number is",num1 / num2)
     print(round(num1/num2,2))
     break
   else:
     print("invalid input")
