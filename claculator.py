#function to add a number to the base
def add(numberToAdd):
  global baseNumber
  baseNumber += numberToAdd
  print("= " + str(baseNumber))

#function to minus a number to the base
def minus(numberToSubtract):
  global baseNumber
  baseNumber -= numberToSubtract
  print("= " + str(baseNumber))

#function to times a number to the base
def times(numberToMultiply):
  global baseNumber
  baseNumber *= numberToMultiply
  print("= " + str(baseNumber))

#function to divide the base by a number
def divide(numberToDivide):
  global baseNumber
  baseNumber /= numberToDivide
  print("= " + str(baseNumber))

#function to list all the options
def list():
  print(
  """
  add
  times
  minus
  divide
  quit
  """)

#provide a welcome message
print("Welcome to the Python calculator.")

#get the base number 
baseNumber = int(input("First enter a number to start with: "))

#loop forever
while True:
  #ask for the opperation
  op = input("For a list of available opperations use 'list' or select operation: ")

  #ask for a second number to apply the operation
  secondNumber = int(input("Enter the second number: "))

  #call the operation function if the operation matches
  if(op == "add" or op == "+"):
    add(secondNumber)
  elif (op == "times" or op ==  "*"):
    times(secondNumber)
  elif (op == "divide" or op == "/"):
    divide(secondNumber)
  elif (op == "minus" or op == "-"):
    minus(secondNumber)
  elif op == "list" :
    list()
  elif op == "quit":
    exit(0)
  #a catch all if the user supplies an invalid operation
  else:
    exit(-1)