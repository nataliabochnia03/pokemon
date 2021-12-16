import matplotlib.pyplot as plt

def pie_chart(pokedex = []):
    """
    Task 27: Create a Pie Chart showing pokemon from pokedex sorted by their generation

    Access the pokedex, sort out pokemon by generation and plot this data in a
    pie chart format. Add labels to clearly identify each generation.

    :param pokedex: list of pokemon
    :return: None
    """
    dicto = {}
    for pokemon in pokedex:
        dicto[pokemon[11]] = dicto.get(pokemon[11], 0) + 1
    data = dicto.values()
    l = [f"Generation {x}" for x in dicto.keys()]
    plt.pie(data, labels=l, autopct="%1.0f%%")
    plt.show(block = False)
    plt.pause(0.01)
    input()
    plt.close()


def bar_chart(pokedex = []):
    """
    Task 28: Create a Bar Chart showing pokemon from pokedex sorted by their type

    Access the pokedex, sort out pokemon by type and plot this data in a
    bar chart format. Add axis labels and main title.

    :param pokedex: list of pokemon
    :return: None
    """
    dicto = {}
    for pokemon in pokedex:
        dicto[pokemon[2]] = dicto.get(pokemon[2], 0) + 1
    x = dicto.keys()
    y = dicto.values()
    plt.bar(x,y)
    plt.title("My Pokemon (Sorted by Type)")
    plt.xlable("Types of Pokemon")
    plt.ylable("Number")
    plt.show(block = False)
    plt.pause(0.01)
    input()
    plt.close()

