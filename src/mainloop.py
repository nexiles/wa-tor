# -*- coding: utf-8 -*-

import random

size_x = 5
size_y = 4

nfische = 13
nhaie   = 7

hbrut   = 8
fasten  = 5
fbrut   = 3


def init_welt(nfische, nhaie):
    """init_welt() -> welt

    Initialisiert eine neue welt.  Gibt die Welt zurück.

    random.choice ...

    """
    welt = []

    # schritt 1: erzeuge eine **leere** welt

    # für jede zeile (y)
        # erzeuge ein neues array für die zeile
        # füge die zeile in die welt

    # für alle zu erzeugenden fische
        # wähle eine zufällige x,y position
        # wenn position nich besetzt:
            # setze den fisch

    # für alle zu erzeugenden haie
        # wähle eine zufällige x,y position
        # wenn position nich besetzt:
            # setze den hai

    return welt

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
    ist_simulation_fertig() -> stopp the loop
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

    The main loop of wa-tor.
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
