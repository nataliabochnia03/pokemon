'''Task 0: Import the modules csv and random'''
import csv, random

def startup():    
    """
    Task 1: Display an entry message.

    The message should consist of the of the name of your application centered in the middle of the console.

    :return: Does not return anything.
    """
    print("\t\t\t\t\t\t\t\t\t\tWelcome in Pokemon APP!")


def options():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Check your Pokemon', 'Add a new Pokemon', 'Show all Pokemon', 'Visualise' ,'Save your Pokedex' and 'Exit'

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    print("Choose one of the options:\n1 = Check your pokemon\n2 = Add new pokemon\n3 = Show all pokemon\n4 = Visualise\n5 = Save your Pokedex\n6 = Exit")
    opt = int(input())
    if opt in {1,2,3,4,5,6}:
        return opt
    else:
        return None


def check_poke():
    """
    Task 3: Display a menu of options for how a Pokemon should be searched. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By name', 'By type'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("Choose one of the options:\n1 = By name \n2 = By type")
    opt = int(input())
    if opt in {1,2}:
        return opt
    else:
        return None

def add_poke():
    """
    Task 4: Display a menu of options for how a Pokemon should be added. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Add specific', 'Add at random'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("Choose one of the options:\n1 = Add specific\n2 = Add at random")
    opt = int(input())
    if opt in {1,2}:
        return opt
    else:
        return None

def visualise():
    """
    Task 5: Display a menu of options for how a graph should be produced. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By Generation (Pie Chart)', 'By Type (Bar Chart)'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("Choose one of the options:\n1 = By generation (Pie Chart)\n2 = By type(Bar Chart)")
    opt = int(input())
    if opt in {1,2}:
        return opt
    else:
        return None
def by_name(p_list = []):
    
    """
    Task 6: Display a pokemon from the list, searching by name.

    The p_list is a list of pokemon.
    Prompt the user to enter name of the pokemon they are searching for.
    The function should display all the details related only to that single pokemon, if it's on the p_list.
    If pokemon of such name does not exist on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    p_name = input("Enter the name of the pokemon: ")
    for pokemon in p_list:
        if pokemon[1] == p_name:
            print(pokemon)
        return
    print("Pokemon does not exist on the list")


def by_type(p_list = []):
    
    """
    Task 7: Display pokemon from the list, searching by type.

    The p_list is a list of pokemon.
    Prompt the user to enter type of the pokemon they are searching for.
    The function should display all the details related only to pokemon of that type,
    if it's on the p_list.
    If no such pokemon of that type exists on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    p_type = input("Enter the type of the pokemon: ")
    for pokemon in p_list:
        if pokemon[2] == p_type or pokemon[3] == p_type:
            print(pokemon)
        return
    print("Pokemon does not exist on the list")

def add_specific_poke():
    
    """
    Task 8: Search for pokemon in the database, and return it if it's found.

    Access pokemon_database.csv using appropriate module.
    Search through this database, looking for a pokemon by it's name.
    If no such pokemon exists, then display appropriate message and return None.

    :param: None
    :return: A list representing a pokemon or None
    """
    with open("pokemon_database.csv") as database:
        reader = csv.reader(database)
        p_name = input("Enter name of the pokemon: ")
        for pokemon in reader:
            if pokemon[1] == p_name:
                return pokemon
        print("Pokemon not found!")
def add_random_poke():
    
    """
    Task 9: Search for a random pokemon in the database, and return it.

    Access pokemon_database.csv using appropriate module.
    Pick out a random pokemon and return it.

    :param:  None
    :return: A list representing a pokemon
    """
    with open("pokemon_database.csv") as database:
        reader = csv.reader(database)
        number = random.randint(1, 801)
        poke_list = []
        for pokemon in reader:
            poke_list.append(pokemon)
        return poke_list[number]

        print("Pokemon not found!")
def show_all(pokedex = []):
    """
    Task 10: Print all pokemon from pokedex.

    Print key information about all the pokemon in the pokedex. Include their
    name, type, total, hp and generation.

    :param p_list: None
    :return: None
    """
    for pokemon in pokedex:
        print(f"Name: {pokemon[1]}\nType: {pokemon[2]} {pokemon[3]}\nTotal: {pokemon[4]}\nHP: {pokemon[5]}\nGeneration {pokemon[11]}")
        print()
def save_pokes(pokedex = []):
    """
    Task 11: Save content of the pokedex to a suitable file format
    Print "Saving complete" at the end.

    :param p_list: pokedex: a list of pokemon
    :return: None
    """
    with open("pokedex.csv", "w", newline= "") as pdex:
        writer = csv.writer(pdex)
        for pokemon in pokedex:
            writer.writerow(pokemon)
        print("Sawing Complete")


def load_pokes(path):
    """
    Task 11.5: Load up pokemon from a CSV file into a list structure
    :param path: A relative file path to CSV file in string format
    :return: A list of pokemon
    """
    p_list = []
    with open(path) as f:
        reader = csv.reader(f)
        for pokemon in reader:
            p_list.append(pokemon)
    return p_list
