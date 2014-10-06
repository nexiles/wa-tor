def main(rounds, nfish, nshark, fbrut, hbrut, fasten):
  return -1
  #start_game(rounds) -> void
  #
  #:rounds: a number which descibes the rounds simulating
  #
  #This is the main funcation of our application, here we start the app and loop the
  #simulation rounds.

  # 1 Round = 1 time unit (Zeiteinheit)

  #1. fische schwimmen und vermehren sich
  #2. haie jagen und vermehren sich
  #3. anzeige

def create_ocean():
  return -1
  #
  #on each grid point can only be one fish or only one shark
  #grid is stapled so -> when the shark or fish want to swim on one side he
  #comes out on the opposite side out again.
  #


def create_fish(id):
  return -1
  #create_fish(id) -> a dict
  #
  #This function creates a fish objcet which we can place in our ocean.
  #
  #The fish object should look like this.
  #
  # {
  #  "id": id,
  #  "cordinates":
  # }
  #

def create_shark(id):
  return -1
  #create_shark(id) -> a dict
  #
  #This function crea a shark objectwhich we can place in our ocean.
  #
  #The shark object should look like this.
  # {
  #  "id": id,
  #   "cordiantes":
  # }
  #



#nfish = Anzahl der Fische am Anfang
#fbrut = Zahl die ein Fisch exestieren muss bis er ein Nachkommen hat

def fish(nfish, fbrut):
  return -1
  #{
  # "nfish": 100,
  # "fbrut": 4
  #}

#if fbrut > 4:
  #print create_fish

#nshark = Anzahl der Haie am Anfang
#sbrut = Zahl die ein Hai exestieren muss bis er ein Nachkommen hat
#fasten = Die Zahl die ein Hai ohne Nahrungs auskommt

def shark(nshark, sbrut, fasten):
  return -1
  #{
  # "nshark": 10,
  # "sbrut": 5
  # "fasten": 4
  #}

#if sbrut > 5:
   #print create_shark

#for every period, while the shark doesnt find a fish, he losing an energy point.
#if the shark find a fish, his energy value increases of the fish enegry.
#
#
def is_fish(X,Y):
  return -1
# returns -1 if no fish otherwise the age of fish

def is_shark(X,Y):
  return -1
# returns -1 if no fish otherwise the age of shark

def fish_swim(X,Y):
  return -1
#um zu wissen ob das ein Ziel von einem anderen Fisch ist in der aktuellen Schleife

def shark_swim(X,Y):
  return -1
#um zu wissen ob das ein Ziel von einem anderen Fisch ist in der aktuellen Schleife

def hungry(X,Y):
  return -1
#um zu wissen ob an dem gitterpunkt ein hai ist und um zu wissen wann er das letzte mal gegessen hat


rounds = 6
nfish = 20
nshark = 5
fbrut = 3
hbrut = 3
fasten = 5
main(rounds, nfish, nshark, fbrut, hbrut, fasten)
