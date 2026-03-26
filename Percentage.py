print("Input your marks of some subjects:")
English = int(input("Enter your english marks:"))
Math = int(input("Enter your maths marks:"))
Science = int(input("Enter your science marks:"))
Computer = int(input("Enter your computer marks:"))

sum = (English+Math+Science+Computer)
print("The sum of your marks is :", sum)
percentage = (sum/400)*100
print("your percentage is:", percentage )
