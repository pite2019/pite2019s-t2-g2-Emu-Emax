from System import System

def main():
    b1 = System.create_bank("PKO")
    b2 = System.create_bank("MBank")
    b3 = System.create_bank("Millenium")
    System.allocate_customers("clients_list.JSON", b1, b2, b3)

    print(b1)
    print(b2)
    print(b3)

    b1.deposit("Karol",130)
    b2.withdraw("Robert",1200)
    b3.credit("Maciek",100)
    b1.investment("Julia",130)
    b2.withdraw("Ola",1200)
    b3.credit("Tymon",100)
    b1.deposit("Dorian",130)
    b2.investment("Ola",1200)
    b3.withdraw("Krystian",1200)


if __name__ == "__main__":
    main()