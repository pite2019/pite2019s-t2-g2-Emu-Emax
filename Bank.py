from Client import Client

class Bank:

    def __init__(self, bank_name):
        self._bank_name = bank_name
        self.client_list = []

    def add_client(self, client_name, client_money = 0):
        new_client = Client(client_name,client_money)
        self.client_list.append(new_client)
            
    def cash_input(self, client_name,cash_value):
        for n in self.client_list:
            if n._client_name == client_name:
                n._client_money += cash_value
    
    def cash_withdraw(self, client_name,cash_value):
        for n in self.client_list:
            if n._client_name == client_name:
                n._client_money -= cash_value
    
    def cash_report(self, client_name):
        for n in self.client_list:
            if n._client_name == client_name:
                self.print_client(n)
    
    def print_client(self, client):
        print("client name: " + str(client._client_name))
        print("client cash: " + str(client._client_money))


