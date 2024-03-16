from math_operations import add, subtract, multiply, divide
from string_operations import concatenate, string_length, to_uppercase, to_lowercase

def main():
    print("Кош келиниз ")
    print("1: Матемитика ")
    print("2: Строка ")

    choice = input("Тандоо ")

    if choice == "1":
        print("1: КОШУУ")
        print("2: Кемитуу")
        print("3: Кобойтуу")
        print("4: Болуу")

        operation = input("Тандоо ")

        a = float(input("А = "))
        b = float(input("B = "))

        if operation == "1":
            print(add(a, b))
        elif operation == "2":
            print(subtract(a, b))
        elif operation == "3":
            print(multiply(a, b))
        elif operation == "4":
            print(divide(a, b))
        else:
            print("ERROR")


    elif choice == "2":
        print("1: concate")
        print("2: len")
        print("3: upper")
        print("4: lower")

        operation = input("Тандоо  ")
        s = input("Строка : ")

        if operation == "1":
            s2 = input("Строка2 :")
            print(concatenate(s, s2))
        elif operation == "2":
            print(string_length(s))
        elif operation == "3":
            print(to_uppercase(s))
        elif operation == "4":
            print(to_lowercase(s))
        else:
            print("ERROR")

if __name__ == "__main__":
    main()
