=======
Wa-Tor
=======


Introduction
============

Wa-Tor is a simulation which simulates the feeding- and reproductive behavior of sharks and fish.
Sharks feed on the fish and the food of the fish is unknown.
That the simulation works, there are some rules:
The Ocean consists of a square Grid. The opposite Sides are stapled. That means that when the shark or 
fish want to swim on 
one side he comes out on the opposite side out again.

***rules for fish:***
Each fish swims randomly to one of the four fields, if it is empty. Each fish has an age, exeeds this 
age the "Breed Time", so 
a new fish is born on an empty field.

***rules for sharks:***
sharks feed on the fish. If a shark don´t find a fish on an adjacent field, so he swims to one of the  free, 
adjacent fields.
Sharks reproduce exactly the same way as a fish.



Requirements
============

- for Mac and possibly for Windows

- language: Python

- Documentation


Goals
=====

- a window with the simulation

- a header

- under the heading, the number of steps (simulations time)
