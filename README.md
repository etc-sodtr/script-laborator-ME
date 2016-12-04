# script-laborator-ME
pentru a nu deschide/inchide 120 fisiere pentru laboratorul de **"Management energetic pentru sisteme fotovoltaice"**

#h2 Introducere:

In acest repo gasiti un script scris in Python, care va va ajuta la extragerea unor date necesare pentru laboratorul de management energetic intitulat "Management energetic pentru sisteme fotovoltaice".

#h2 Pretext

La acest laborator, printre altele, trebuie sa extragem din seria de fisiere .lvm primite(existente pe calculatoarele din laborator in folderul *Master 2016*, valorile puterii maxime debitate de celula de Siliciu monocristalin (care sunt cuprinse in fisierele de tip *I-V PV_1 999999 xxx.lvm* ) si valorile puterii maxime debitate de celula de Siliciu amorf (care sunt cuprinse in fisierele de tip *I-V PV_2 999999 xxx.lvm* ).

 Trebuie ca fiecare sa alegem o zi(vedeti data crearii fisierelor), si pentru aceasta zi sa extragem informatia despre puterea maxima din toate fisierele aflate intre orele 10 si 14:55. Acestor valori trebuie sa le facem media pe ore. Mai jos aveti si un exemplu

![alt text][logo]

[logo]: https://github.com/etc-sodtr/script-laborator-ME/blob/master/exemplu.JPG "exemplu"

#h2 utilizarea programului

Am creat un folder (am folosit sistemul de operare Linux pentru rularea codului de Python) in care am introdus cele 60 de fisiere aferente celulei de siliciu monocristalin si scriptul *me3_final.py*. Apoi am deschis o consola si cu comanda `cd` m-am dus in folderul respectiv (scuze ca dau atatea detalii). apoi am rulat scriptul cu comanda `python me3_final.py` . Acest lucru trebuie facut si pentru cele 60 de fisiere aferente celulei de siliciu amorf.

**Nota:** Daca aveti instalat in linux Python 3, atunci  veti inlocui prima linie a scriptului cu `#!/usr/bin/env python3` si veti folosi comanda de rulare `python3 me3_final.py` .

SPOR!

