from pojistenec import Pojistenci
import os

#starting aplication
starter = True
evidenc = []
while starter:
    #clearing screen, start text
    os.system('clear')
    print('----------------------------\nEvidence pojištěných\n----------------------------\n')
    #chosing requierement
    print('Vyberte si akci:')
    print('1 - Přidat nového pojištěnce')
    print('2 - Vypsat všechny pojištěné')
    print('3 - Vyhledat pojištěného')
    print('4 - Konec')

    chosed = int(input())
    print()

    #adding new insured
    if chosed == 1:
        name = input('Zadejte jméno: ')
        lastname = input('Zadejte příjmení: ')
        age = int(input('Zadejte věk: '))
        telephone = input('Zadejte telefoní číslo: ')
        new_insured = Pojistenci(name, lastname, age, telephone)
        evidenc.append(new_insured)
        print('\nData byla uložena.\n')

    #write list of all insured people
    if chosed == 2:
        for insured in evidenc:
            print(insured)
        print('\nToto jsou všichni evidovaní pojištěnci\n')

    #find insured by name or lastname
    if chosed == 3:
        name = input('Zadejte jméno hledaného pojištěnce: ')
        lastname = input('Zadejte příjmenení hledaného pojištěnce: ')
        for insured in evidenc:
            if insured.name == name and insured.lastname == lastname:
                print(f'\n{insured}\n')

    #exit
    if chosed == 4:
        starter = False
        print('děkujeme vám za využití aplikace a brzy nashledanou\n')
    
    #waiting for next requirement and clearing the screen
    input('Pokračjete libovolnou klávesou...')
    os.system('clear')