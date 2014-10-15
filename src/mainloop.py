# -*- coding: utf-8 -*-

import random

size_y = 8
size_x = 9

nfische = 4
nhaie   = 6

hbrut   = 8
fasten  = 5
fbrut   = 3


def init_welt(nfische, nhaie):
    """init_welt() -> welt

    Initialisiert eine neue welt.  Gibt die Welt zurück.

    random.choice ...

    """
    welt = {}
    for zeile in range(size_y):
        welt[zeile] = []
        for spalte in range(size_x):
            zeilen_array = welt[zeile]
            zeilen_array.append([0])
    # schritt 1: erzeuge eine **leere** welt

    # für jede zeile (y)
        # erzeuge ein neues array für die zeile
        # füge die zeile in die welt


    fisch = create_fish()
    for i in range(nfische):
        #erster durchlauf i=1
        #
        welt = set_gameobject_in_world(fisch, welt)

    for i in range(nhaie):
        shark = create_shark()
        welt = set_gameobject_in_world(shark, welt)

    return welt

def set_gameobject_in_world(typ, welt):
    """Der Fisch oder Hai wird in die Welt eingesetzt wenn der Punkt nicht
    besetzt ist.
    """
    # wähle eine zufällige x,y position
    # wenn position nich besetzt:
        # setze den hai/fisch

    x, y = get_random_pos()
    if is_already_set(x, y, welt):
        welt = set_gameobject(x, y, welt, typ)

    else:
        set_gameobject_in_world(typ, welt)
    return welt

def set_gameobject(x, y, welt, value):
    welt[y][x] = value
    return welt

def is_already_set(x, y, welt):
    """is_already_set(x, y, welt)-> bool
    :x: the x cordinate we want to set
    :y: the y cordinate we want to set
    :welt: an array which includes several arrays. represending the world

    1/3 =

    :return: True/False wenn der Punkt besetzt ist
    """
    if (welt[y][x][0] == 0):
        return True
    else:
        return False

def create_fish():
    """
    create_fish() -> fish
    Erstellt einen Fisch mit einer zufällig gewählten Alters-Zahl.
    """
    return [1, random.randint(1, 2)]

def create_shark():
    """
    create_shark() -> shark
    Erstellt einen Hai mit einer zufällig gewälten Alters-Zahl und einer
    Fasten-Zahl
    """
    return [2, random.randint(1,7), random.randint(1,4)]

def get_random_pos():
    """Es wird eine zufällige Position für den Fisch und für
    den Hai ausgewählt.
    """
    y = random.randint(0, 7)
    x = random.randint(0, 8)
    return (x, y)

def simulationsschritt(t, welt):
    """
    simulationsschritt(t, welt) -> welt

    Simuliert die welt und gibt die neue welt
    als ergebnis.
    """
    return welt

def display(t, welt):
    """
    display(t, welt) -> None

    Stelle die aktuelle welt und zeit dar.
    """
    print "Time: ", t
    for y in range(size_y):
        for x in range(size_x):
            print " ", welt[y][x], " ",
        print


def ist_simulation_fertig(dt, t, t_stopp):
    """
    ist_simulation_fertig() -> stopt die Schleife
    """
    fertig = False
    if dt < 0:
        if t <= t_stopp:
            fertig = True

    else:
        if t >= t_stopp:
            fertig = True

    return fertig


def mainloop(t_start, dt, t_stopp):
    """
    mainloop

    Die Hauptschleife von Wa-Tor.
    """
    # initialisiere die zeit
    t = t_start

    # initialisiere eine welt
    welt = init_welt(nfische, nhaie)

    #pdb.set_trace()

    fertig = False
    # solange nicht fertig:
    while not fertig:
        # simuliere die welt
        welt = simulationsschritt(t, welt)

        # welt darstellen
        display(t, welt)

        # zeit erhöhen
        t = t + dt

        # Wenn die Zeit t_stopp erreicht ist, bitte aufhoeren
        fertig = ist_simulation_fertig(dt ,t ,t_stopp)

    return t

print "Runde 1"
mainloop(0, 1, 5)

print "Runde 2"
mainloop(0, 1, 3)

print "Runde 3"
mainloop(-3, 1, 0)

print "Runde 4"
mainloop(3, -1, 0)

print "Runde 5"
mainloop(10, -2, 5)

print "Runde 6"
mainloop(6, -0.5, 4)
