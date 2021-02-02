from art import logo
print(logo)

def add(n1,n2):
  """Input two numbers to add them."""
  return n1+n2
def sub(n1,n2):
  return n1-n2
def multi(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2

operations={
  "+": add,
  "-": sub,
  "*": multi,
  "/": div,
}
def calculator():
  num1=int(input("What is the first number: "))
  print("Pick an operation:")
  for item in operations:
    print(item)
  operation_symbol=input("You choose: ")
  num2=int(input("What is te second number: "))

  calculation_function=operations[operation_symbol]
  answer=calculation_function(num1,num2)
  print(f"{num1} {operation_symbol} {num2}= {answer}")
  ending=input(f"Type 'y' to continue calculating with {answer} or 'n' to to exit.");
  if ending=="y":
    while ending!="n":
      operation_symbol=input("Pick an operation: ")
      num3=int(input("What is the next number:"))
      calculation_function=operations[operation_symbol]
      second_answer=calculation_function(answer,num3)
      print(f"{answer} {operation_symbol} {num3}= {second_answer}")
      ending=input(f"Type 'y' to continue calculating with {answer} or 'n' to to exit.");
  elif ending=="n":
    calculator()

calculator()