# calculator
from replit import clear
import art
# Add
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# create a Dictionary "operation" and store operators as key and output as value

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  print(art.logo)
  num1 = float(input("Enter the first number: "))
  
  
  for operation in operations:
    print(operation)
  continue_calculate_number = True
  while continue_calculate_number:
    operation_symbol = input("Pick an operator: ")
    num2 = float(input("Enter the next number: "))
    
    calculator_function = operations[operation_symbol]
    result = calculator_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {result}")
    
    continue_calculate = input(f"Type 'y' to continue calculating with {result} or type 'n' to exit: ")
    if continue_calculate == "y":
      num1 = result
    else:
      continue_calculate_number = False
      clear()
      calculator()
calculator()

  
  
  



