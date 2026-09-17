
def calculator(a,b,operator):
     match operator:
      case "+":
       return a+b
      case "-":
       return a-b
      case "*":
             return a*b
      case "/":
             return a/b
      case _:
             return "invalid op"   
       


a=int(input("Enter First number:"))
b=int(input("Enter second number:"))
op=(input("Enter the operator(+,-,*,/):")
print("The result is ",calculator(a,b,operator))


