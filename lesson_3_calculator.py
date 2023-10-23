value_int_1 = 0
value_int_2 = 0
result = 0
choose = True

while choose:
 try:
  value_int_1 = int(input("Choose first type of number: "))
  value_int_2 = int(input("Choose second type of number: "))
 except ValueError:
    print("Wrong type of number")

 value_operator = input("Choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n : ")

 if value_operator == "1":
    result = value_int_1 + value_int_2
 elif value_operator == "2":
    result = value_int_1 - value_int_2
 elif value_operator == "3":
    result = value_int_1 * value_int_2
 elif value_operator == "4":
  try:
    result = value_int_1 / value_int_2
  except ZeroDivisionError:
        print("You cant divide on zero")
  else:
    print("Incorrect operator")

 print(result)

 print("Do you want to use program again?")

 choose = input("Answer 'Yes' or 'No'")

 if choose == "No":
  print("Thanks for using our product, have a nice day!")
  choose = False
  break
 elif choose == "Yes":
  continue
 else:
  print("Incorrect answer")