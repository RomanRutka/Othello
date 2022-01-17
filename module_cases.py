class Case:
    # Construction des objets "Cases", deux attributs correspond à leur position
    def __init__(self, x, y):
        self.ligne = x
        self.position = y

    def __str__(self):
        return "   "

class CaseVide(Case):
    # Construction de cases vides
    def __init__(self, x, y):
        super().__init__(x, y)
        # les cases peuvent être accessibles/jouables ou pas - par défaut elles ne sont pas jouables
        # les cases peuvent être des pions vides, blancs, ou noirs (0, 1, 2)
        self.etat = 0
        self.acces = False


class PionBlanc(Case):
    # Construction de cases à pions blancs
    def __init__(self, x, y):
        super().__init__(x, y)
        self.etat = 1
        self.acces = False
    
    def __str__(self): # l'appel de str(NOMDELACASE) retourne O
        return " O "

class PionNoir(Case):
    # Construction de cases à pions noirs
    def __init__(self, x, y):
        super().__init__(x, y)
        self.etat = 2
        self.acces = False

    def __str__(self) : # l'appel de str(NOMDELACASE) retourne X
        return " X "

# methode qui teste l'accessibilité de la case
def est_jouable():
    pass


# methode qui pose le pion
def modif_etat(x, y):
    pass

