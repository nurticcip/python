first_number = int(input("Add first number: "))
second_number = int(input("Add second number: "))
action = input("Add action: ")
if action == '+':
    print('Result: ', first_number + second_number)
elif action == '-':
    print('Result: ', first_number - second_number)
elif action == '*':
    print('Result: ', first_number * second_number)
elif action == '/':
    print('Result: ', first_number / second_number)
elif action == '^':
    print('Result: ', first_number ** second_number)
else:
    print("ERROR")