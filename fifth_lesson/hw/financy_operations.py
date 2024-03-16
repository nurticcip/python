class Finance:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []
    def income(self, amount, description):
        self.balance += amount
        self.transactions.append(f'Киреше: {amount: .2f} ({description})') 
    def expense(self, amount, description):
        self.balance -= amount
        self.transactions.append(f'Керектоо: -{amount: .2f} ({description})')
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        return self.transactions