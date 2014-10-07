"""
nfish = Anzahl der Fische am Anfang

fbrut = Zahl die ein Fisch exestieren muss bis er ein Nachkommen hat
"""

def main(rounds, nfish, nshark, fbrut, hbrut, fasten):
    """
    start_game(rounds) -> void

    :rounds: a number which descibes the rounds simulating

    This is the main funcation of our application, here we start the app and
    loop the simulation rounds.

    1 Round = 1 time unit (Zeiteinheit)

    1. fische schwimmen und vermehren sich
    2. haie jagen und vermehren sich
    3. anzeige
    """
    return -1

def create_ocean():
    """
    on each grid point can only be one fish or only one shark
    grid is stapled so -> when the shark or fish want to swim on one side he
    comes out on the opposite side out again.
    """
    return -1


def create_fish(id):
    """
    create_fish(id) -> a dict

    This function creates a fish objcet which we can place in our ocean.

    @param id: the id of a new fish

    @returns: a fish
    """
    #
    #The fish object should look like this.
    #
    # {
    #  "id": id,
    #  "cordinates":
    # }
    #
    return -1

def create_shark(id):
    """
    create_shark(id) -> a dict

    This function creates a shark object which we can place in our ocean.

    @param id: the id of a new shark

    @returns:  a shark
    """
    #
    #The shark object should look like this.
    # {
    #  "id": id,
    #   "cordiantes":
    # }
    #
    return -1


def fish(nfish, fbrut):
    """
    "nfish": number,
    "fbrut": number

    This function gives the number of the fishes in the beginning and the
    number when a fish get a progeny.

    When the number is bigger than the fbrut number, a new fish will create.
    """
    return -1

    # Example
    #
    #if fbrut > 4:
        #print create_fish


def shark(nshark, sbrut, fasten):

    """
    "nshark": number,
    "sbrut": number
    "fasten": number

    This function gives the number of the fishes in the beginning, the
    number when a shark get a progeny and the number survive the sharks
    without food.


    When the number is bigger than the fbrut number, a new shark will create.
    When the number is bigger than the fasten number, the shark dies.
    """
    return -1

    # Example
    #if sbrut > 5:
        #print create_shark
    #
    #if fasten < 4
        #shark dies

    #for every period, while the shark doesnt find a fish, he losing an energy
    #point.
    #if the shark find a fish, his energy value increases of the fish enegry.
    #

def is_fish(X,Y):
    """
    returns -1 if no fish otherwise the age of fish
    """
    return -1

def is_shark(X,Y):
    """
    returns -1 if no fish otherwise the age of shark
    """
    return -1

def fish_swim(X,Y):
    """
    um zu wissen ob das ein Ziel von einem anderen Fisch ist in der aktuellen
    Schleife
    """
    return -1

def shark_swim(X,Y):
    """
    um zu wissen ob das ein Ziel von einem anderen Hai ist in der aktuellen
    Schleife
    """
    return -1

def hungry(X,Y):
    """
    um zu wissen ob an dem gitterpunkt ein hai ist und um zu wissen wann er das
    letzte mal gegessen hat
    """
    return -1

rounds = 6
nfish = 20
nshark = 5
fbrut = 3
hbrut = 3
fasten = 5
main(rounds, nfish, nshark, fbrut, hbrut, fasten)
