from model.Lalana import Lalana

class Simba:
    def __init__(self, lalana: Lalana, pk_debut: float, pk_fin: float, niveau: int) -> None:
        self.set_lalana(lalana)
        self.set_pk_debut(pk_debut) # km
        self.set_pk_fin(pk_fin)     # km
        self.set_niveau(niveau)

    def calc_cout(self, prix_metre_cube: float) -> float:
        return self.calc_volume() * prix_metre_cube

    def calc_volume(self) -> float:
        longueur = (self.get_pk_fin() - self.get_pk_debut()) * 1000     # m
        profondeur = (self.get_niveau() / 10)                           # cm
        profondeur /= 100                                               # m
        return longueur * profondeur * self.get_lalana().get_largeur()  # m3

    def calc_duration(self, duree_metre_cube: float) -> float:
        return self.calc_volume() * duree_metre_cube

    def get_lalana(self) -> Lalana:
        return self.__lalana
    
    def set_lalana(self, value: Lalana):
        self.__lalana = value

    def get_pk_debut(self) -> float:
        return self.__pk_debut
    
    def set_pk_debut(self, value: float):
        self.__pk_debut = value
    
    def get_pk_fin(self) -> float:
        return self.__pk_fin
    
    def set_pk_fin(self, value: float):
        self.__pk_fin = value
    
    def get_niveau(self) -> int:
        return self.__niveau
    
    def set_niveau(self, value: int):
        if not value >= 0 or not value <= 100:
            raise Exception("Not valid")
        self.__niveau = value
