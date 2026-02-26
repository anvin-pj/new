#calculator
import sys
while True:
    total=0
    try:
        num1=int(input("enter the first number"))
        num2=int(input("enter the 2nd number"))
        op=input("enter the operator[+,-,*,/,%]")
        if op=="+":
            total=num1+num2
            
        elif op=="-":
            total=num1-num2
            
        elif op=="*":
            total=num1*num2
               
        elif op=="%":
            total=num1%num2
           
        elif op=="/":
            total=num1/num2
            
        else:
            print("invalid operator")
            continue
        print("{}{}{}={}".format(num1,op,num2,total))
        break
    except:
        print("oops",sys.exc_info(),"occured")

