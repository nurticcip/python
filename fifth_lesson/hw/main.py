from financy_operations import Finance

def main():
    tracer = Finance()

    while True:
        print("бюджетти эсепке алуу системасы")
        print("1. киреше")
        print("2. керектоо")
        print("3. баланс")
        print("4. транзакциянын тарыхын коруу")
        print("5. чыгуу")

        choise = input("бир вариянтты танданыз: ")

        if choise == "1":
            amount = float(input("кирешенин суммасын киргизиниз: "))
            description = input("сыпаттоо: ")
            tracer.income(amount,description)
            print(f"киреше {amount}  сом")
            print("киреше катталды")
            print("/n")

        elif choise == "2":
            amount = float(input("чыгымдын суммасын киргизиниз: "))
            description = input("сыпаттоо: ")
            tracer.expense(amount,description)
            print(f"чыгым {amount}  сом")
            print("чыгым катталды")

        elif choise == "3":
            print(f"баланс: {tracer.get_balance():.2f} сом")

        elif choise == "4":
            print("транзакциянын тарыхын")
            for transaction in tracer.transaction_history():
                print(transaction)

        elif choise == "5":
            print("программадан чыгуу.")
            break
        else:
            print("ката")


if __name__ == "__main__":
    main()