from Client import Client

class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.client_list = []
        self.CREDIT_MULTIPLIER = 5
        self.CREDIT_PERCENTAGE = 0.05

    def add_client(self, client_name, client_money = 0):
        new_client = Client(client_name,client_money)
        self.client_list.append(new_client)
            
    def deposit(self, client_name, cash_value):
        for n in self.client_list:
            if n.client_name == client_name:
                n.client_money += int(cash_value)
    
    def withdraw(self, client_name,cash_value):
        for n in self.client_list:
            if n.client_name == client_name:
                if (n.client_money - cash_value) > 0:
                    n.client_money -= cash_value
                else:
                    Bank.log("Cannot withdraw! ")
    
    def credit(self, client_name,cash_value):
        for n in self.client_list:
            if n.client_name == client_name:
                if (cash_value * self.CREDIT_MULTIPLIER) > n.client_money:
                    Bank.log("Cannot credit, too small capital! ")
                else:
                    n.client_money += cash_value
                    perc = self.CREDIT_PERCENTAGE * cash_value
                    n.client_money -= perc
                    Bank.log(f"Credit accepted! Borrowed money: {cash_value}")
    
    def investment(self, client_name,cash_value):
        for n in self.client_list:
            if n.client_name == client_name:
                if cash_value > n.client_money:
                    Bank.log("Too small capital for investment! ")
                else:
                    n.client_money -= cash_value
                    perc = self.CREDIT_PERCENTAGE * cash_value
                    n.client_money += perc
                    Bank.log(f"Investment accepted! Monthly percentage: {perc}")
    
    def print_client(self, client):
        print("client name: " + str(client.client_name))
        print("client cash: " + str(client.client_money))
    
    def __str__(self):
        result = "Bank name: " + self.bank_name + " \n"
        for c in self.client_list:
            result += c.client_name + ", money: " + str(c.client_money) + "\n"
        return result

    @staticmethod
    def log(message):
        print("BANK LOG: --" + message)

