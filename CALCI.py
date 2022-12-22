# make a calculator in python

c = input("Enter what you want to do"+ '\n' +
          "+ --> addition"+'\n' +
          "- --> subtraction"+ '\n' +
          "* --> multiplication"+ '\n' +
          "/ --> division"+'\n' +
          "choice :- ")

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

def add(n1,n2):
         res = n1+n2
         print("The sum of ",num1," and ",num2," = ",res)
def sub(n1,n2):
         res = n1-n2
         print("The subtraction of ",num1," and ",num2," = ",res)
def mul(n1,n2):
         res = n1*n2
         print("The product of ",num1," and ",num2," = ",res)
def div(n1,n2):
         res = n1/n2
         print("The division of ",num1," and ",num2," = ",res)

if(c == "+"):
    add(num1,num2)
elif(c=="-"):
    sub(num1,num2)
elif(c=="*"):
    mul(num1,num2)
elif(c=="/"):
    div(num1,num2)
else:
    print("INVALID INPUT")
               
                

                               
           
           
        
         
         
         
         
          
          

          
