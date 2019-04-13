from Bank import Bank
import json

class System:

    @staticmethod
    def create_bank(bank_name):
        new_bank = Bank(bank_name)
        return new_bank
    
    @staticmethod
    def allocate_customers(file_name, *banks):
        no_of_banks = len(banks)
        bank_names = []
        for i in range(no_of_banks):
            bank_names.append(banks[i].bank_name)
        
        with open(file_name) as json_file:
            data = json.load(json_file)
            for client in data:
                no_of_fails = no_of_banks
                for b in banks:
                    if b.bank_name == client['bank']:
                        b.add_client(client['name'],int(client['starting_money']))
                    else:
                        no_of_fails -= 1
                if no_of_fails == 0:
                    System.log(f"Nie ma takiego banku w systemie: {client['bank']}")
                    no_of_fails = no_of_banks

    @staticmethod
    def log(message):
        print("SYSTEM LOG: --" + message)