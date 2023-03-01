from dao.LalanaDAO import LalanaDAO
from dao.PkDAO import PkDAO

class Simba:
    def __init__(self, idSimba: int, idPk_debut: int, idPk_fin: int, niveau: int) -> None:
        self.idSimba = idSimba
        self.idPk_debut = idPk_debut  # km
        self.idPk_fin  = idPk_fin     # km
        self.niveau = niveau

    def calc_cout(self, con) -> float:
        prix_metre_cube = PkDAO.get_prix_metre_cube(con, self.idPk_debut)
        return self.calc_volume(con) * prix_metre_cube

    def calc_volume(self, con) -> float:
        pk_debut = PkDAO.find_by_id(con, self.idPk_debut)
        pk_fin = PkDAO.find_by_id(con, self.idPk_fin)

        lalana = LalanaDAO.find_by_id(con, pk_debut.idLalana)

        longueur = (pk_fin.valeur - pk_debut.valeur) * 1000           # m
        profondeur = (self.niveau / 10)                 # cm
        profondeur /= 100                               # m
        return longueur * profondeur * lalana.largeur   # m3

    def calc_duration(self, con) -> float:
        duree_metre_cube = PkDAO.get_duree_metre_cube(con, self.idPk_debut)
        return self.calc_volume(con) * duree_metre_cube
