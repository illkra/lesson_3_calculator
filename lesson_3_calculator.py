value_int_1 = 0
value_int_2 = 0

try:
    value_int_1 = int(input("Choose first type of number: "))
    value_int_2 = int(input("Choose second type of number: "))
except ValueError:
    print("Wrong type of number")

value_operator = input("Choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n : ")

if value_operator == "1":
    print(value_int_1 + value_int_2)
elif value_operator == "2":
    print(value_int_1 - value_int_2)
elif value_operator == "3":
    print(value_int_1 * value_int_2)
elif value_operator == "4":
    print(value_int_1 / value_int_2)
else:
    print("Incorrect operator")
