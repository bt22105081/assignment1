# program to calculate the gross income tax of a person
income = float(input("Enter the total income upto pennies"))
dep = int(input("enter the number of dependants"))
taxin = income - (10000+3000*dep)
if(taxin <=0):
    print("no tax applicable")
else:
    tax = taxin * 20/100
    print("The tax on your income = " ,tax)
