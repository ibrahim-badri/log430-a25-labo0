<div align="center">

<h1 style="font-size:18pt;">
Laboratoire 0 : Infrastructure (Git, Docker, CI/CD)
</h1>

<br>

<h2 style="font-size:16pt;">
PAR
</h2>

<br>

<h2 style="font-size:16pt;">
Ibrahim BADRI, BADI02089900
</h2>

<br><br>

<h3 style="font-size:14pt;">
RAPPORT DE LABORATOIRE PRÉSENTÉ À MONSIEUR FABIO PETRILLO DANS LE CADRE DU COURS <em>ARCHITECTURE LOGICIELLE</em> (LOG430-02)
</h3>

<br><br>

<h3 style="font-size:14pt;">
MONTRÉAL, LE 13 SEPTEMBRE 2025
</h3>

<br>

<h3 style="font-size:14pt;">
ÉCOLE DE TECHNOLOGIE SUPÉRIEURE<br>
UNIVERSITÉ DU QUÉBEC
</h3>

</div>

---

### Tables des matières 

---

#### Question 1

<div style="text-align: justify;">

> Si l’un des tests échoue à cause d’un _bug_, comment `pytest` signale-t-il l’erreur et aide-t-il à la localiser ?  
> Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

</div>

<div style="text-align: justify;">

Lorsque l’un des tests échoue à cause d’un _bug_, `pytest` l’indique clairement dans le terminal en affichant le nombre total de tests exécutés, réussis et échoués, puis détaille dans la section `FAILURES` le nom de la fonction de test fautive, le fichier et la ligne exacte où l’erreur s’est produite ainsi que le message explicatif qui s’y applique. Dans le cadre de l’exécution de mon test volontairement faux, on obtient le message `DID NOT RAISE <class ‘ZeroDivisionError’>` qui découle d’une division d’un chiffre par zéro $0$. L’échec provient du fait que le code testé renvoie simplement une chaîne de caractères au lieu de lever l’exception attendue, ce qui provoque le décalage entre le contrat du test et le comportement réel de la fonction.



</div>


##### Question 2

##### Question 3

##### Question 4


