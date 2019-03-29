from Bank import Bank

class System:

    @staticmethod
    def create_bank(bank_name):
        new_bank = Bank(bank_name)
        return new_bank