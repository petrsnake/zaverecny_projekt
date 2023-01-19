import os
from database_creator import session, Insurance

# starting aplication
starter = True
evidenc = []
while starter:
    # clearing screen, start text
    os.system('clear')
    print('----------------------------\nEvidence pojištěných\n----------------------------\n')
    # chosing requierement
    print('Vyberte si akci:')
    print('1 - Přidat nového pojištěnce')
    print('2 - Vypsat všechny pojištěné')
    print('3 - Vyhledat pojištěného')
    print('4 - Konec')

    chosed = int(input())
    print()

    # adding new insured
    if chosed == 1:
        name_input = input('Zadejte jméno: ')
        lastname_input = input('Zadejte příjmení: ')
        age_input = int(input('Zadejte věk: '))
        telephone_input = input('Zadejte telefoní číslo: ')
        # adding data of new insurance to session and commit to table of database
        session.add(Insurance(name=name_input, lastname=lastname_input,
                    age=age_input, telephone=telephone_input))
        session.commit()
        print('\nData byla uložena.\n')

    # write list of all insured people
    if chosed == 2:
        all_insured = session.query(Insurance).all()
        for insured in all_insured:
            print(insured)
        print('\nToto jsou všichni evidovaní pojištěnci\n')

    # find insured by name or lastname
    if chosed == 3:
        name_input = input('Zadejte jméno hledaného pojištěnce: ')
        lastname_input = input('Zadejte příjmenení hledaného pojištěnce: ')
        wanted = session.query(Insurance).\
            filter(Insurance.name==name_input,Insurance.lastname==lastname_input).all()
        if not wanted:
            wanted = '\nPojištěnec tohoto jména nebyl nalezen'
        print(f'\n{wanted}\n')

    # exit
    if chosed == 4:
        starter = False
        print('děkujeme vám za využití aplikace a brzy nashledanou\n')

    # waiting for next requirement and clearing the screen
    input('Pokračjete libovolnou klávesou...')
    os.system('clear')
