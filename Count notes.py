Amount = int(input("The amount which is withrawed is:"))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print("The number of 100rs notes are:", note1)
print("The number of 50rs notes are:", note2)
print("The number of 10rs notes are:", note3)
