from module_cases import (Case,
    CaseVide,
    PionBlanc,
    PionNoir)
    
class Board:
    def __init__(self) :
        self.set_liste()
        self.display()
        self.scoreX = 2
        self.scoreY = 2
        # self.liste_cases = []
        # self.set_liste(self.liste_cases)

    def set_liste(self):
        ligne1 = []
        ligne2 = []
        ligne3 = []
        ligne4 = []
        ligne5 = []
        ligne6 = []
        ligne7 = []
        ligne8 = []
        for ligne in range(1, 9):
            for col in range (1, 9):
                if ligne == 1 :
                    case = CaseVide(col-1, ligne-1)
                    ligne1.append(case)
                if ligne == 2 :
                    case = CaseVide(col-1, ligne-1)
                    ligne2.append(case)
                if ligne == 3 :
                    case == CaseVide(col-1, ligne-1)
                    ligne3.append(case)
                if ligne == 4 :
                    case = CaseVide(col-1, ligne-1)
                    ligne4.append(case)
                if ligne == 5 :
                    case = CaseVide(col-1, ligne-1)
                    ligne5.append(case)
                if ligne == 6 :
                    case = CaseVide(col-1, ligne-1)
                    ligne6.append(case)
                if ligne == 7 :
                    case = CaseVide(col-1, ligne-1)
                    ligne7.append(case)
                if ligne == 8 :
                    case = CaseVide(col-1, ligne-1)
                    ligne8.append(case)
        
        self.liste_cases = [ligne1, ligne2, ligne3, ligne4, ligne5, ligne6, ligne7, ligne8]
        self.liste_cases[3][3] = PionBlanc(3, 3)
        self.liste_cases[4][4] = PionBlanc(4, 4)
        self.liste_cases[3][4] = PionNoir(3, 4)
        self.liste_cases[4][3] = PionNoir(4, 3)
        
    
    def display(self):  
        
        print("    ", end ="")
        print("   ".join(list("ABCDEFGH")))
        print("  ", end ="")
        print("---".join("+" * 9))
        for ligne in range (0, 8):
            print(ligne+1,"|", end ="")
            for elem in range (0, 8):
                print(f"{self.liste_cases[ligne][elem]}|", end = "") 
            print()
            print("  ", end ="") 
            print("---".join("+" * 9))

    def modif_case(self, couleur, y, x):
        if couleur == "O":
            self.liste_cases[x-1][y-1] = PionBlanc(x, y)
        else :
            self.liste_cases[x-1][y-1] = PionNoir(x, y)
        self.display()