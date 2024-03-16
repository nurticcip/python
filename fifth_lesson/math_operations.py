class Client:
    # Конструктор класса для инициализации атрибутов
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Метод для пополнения счета
    def deposit(self, amount):
        self.balance += amount
        return f"Баланс пополнен на {amount}. Текущий баланс: {self.balance}"

    # Метод для снятия денег со счета
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Со счета снято {amount}. Текущий баланс: {self.balance}"
        else:
            return f"Недостаточно средств. Текущий баланс: {self.balance}"

# Создание объектов класса Client
client1 = Client("Марлен Канатбеков", 1000)
client2 = Client("Айдана Кубатбекова", 5000)

# Использование методов объектов
print(client2.deposit(500))    # => Баланс пополнен на 500. Текущий баланс: 1500
print(client2.withdraw(200))  # => Со счета снято 2000. Текущий баланс: 3000
