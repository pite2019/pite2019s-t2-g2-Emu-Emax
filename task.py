#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
from System import System


def main():
    b1 = System.create_bank("PKO")

    b1.add_client("Karol",13498)
    b1.add_client("Kuba")

    b1.cash_input("Karol",130)
    b1.cash_report("Karol")
    b1.cash_withdraw("Karol",1200)
    b1.cash_report("Karol")

    b1.cash_report("Kuba")


if __name__ == "__main__":
    main()