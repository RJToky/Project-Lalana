class Lalana:
    def __init__(self, longueur: float, largeur: float) -> None:
        self.set_longueur(longueur)  #km
        self.set_largeur(largeur)    #m

    def get_longueur(self) -> float:
        return self.__longueur
    
    def set_longueur(self, value: float):
        self.__longueur = value

    def get_largeur(self) -> float:
        return self.__largeur
    
    def set_largeur(self, value: float):
        self.__largeur = value
