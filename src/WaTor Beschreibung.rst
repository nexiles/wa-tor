Wa-Tor
======

Beschreibung
-------------

Wa-Tor ist eine Simulation die das Fress- und Fortpflanzungsverhalten von Haien und Fischen
simuliert. Um diese Simulation darstellen zu können muss man diese erst mal programmieren.
Es werden verschiedene Funktionen erstellt z.B. die Funktion **"main"**.
**"main"** ist dazu da damit überhaupt erstmal was aufgerufen wird beziehungsweise das die Simulation starten kann.
In "main" wird die Anzahl der Runden angegeben.
Die Funktion **"create_ocean"** definiert ein paar Regeln. Z.B. kann auf jeden Gitterpunkt nur ein
Fisch oder nur ein Hai sein. Allerdings ist das Gitter auch "verheftet" das heißt wenn ein
Fisch auf einer Seite raus schwimmen will kommt er auf der gegenüberliegenden Seite wieder rein.
Damit überhaupt Fische und Haie existieren müssen diese definiert werden und das wird mit der
Funktion **"create_fish"** und **"create_shark"** gemacht. In dieser Funktion werden unteranderem
die Koordinaten angeben an welchem Gitterpunkt der Hai oder Fisch ist.
Die Funktion **"fish"** mit den parametern **"nfish"** und **"fbrut"** ist dazu da, um die Anzahl der Fische
am Anfang festzulegen. **"fbrut"** ist die Zahl die ein Fisch existieren muss bis er ein Nachkommen hat.
Bei der Funktion **"shark"** mit den parametern **"nshark"**, **"sbrut"** und **"fasten"** ist es genau das
selbe wie bei dem Fisch. Allerdings gibt es hier eine Besonderheit: der parameter **"fasten"**
gibt die Zahl an die ein Hai ohne Nahrung auskommt und wird diese Zahl überschritten stirbt der Hai.
In jedem Zyklus in dem der Hai keinen Fisch findet, verliert er einen Energiepunkt. Findet
der Hai jedoch einen Fisch werden ihm die Energiewerte von dem Fisch dazugerechnet.
**"is_fish"** und **"is_shark"** definiert bzw fragt ob an einem gewissen Gitterpunkt bereits ein Fisch oder
Hai ist. Wenn dort kein Fisch oder Hai ist gibt es -1 zurück. Wenn dort allerdings ein Fisch oder Hai ist,
gibt es das Alter des Fisches oder Haies zurück.
Die Funktion **"fish_swim"** und **"shark_swim"** gibt an ob der Gitterpunkt ein Ziel eines anderen Fisch oder Hai ist
(in der aktuellen Schleife). **"hungry"** gibt an ob an dem Gitterpunkt ein Hai ist und zeigt an wann er das
letzte mal gegessen hat.
Dann werden den Parametern **"rounds"**, **"nfish"**, **"nshark"**, **"fbrut"**, **"hbrut"**
und **"fasten"** jeweils einen Wert zugeordnet.
