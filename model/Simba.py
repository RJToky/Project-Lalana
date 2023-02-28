from dao.LalanaDAO import LalanaDAO
from dao.PkDAO import PkDAO

class Simba:
    def __init__(self, idSimba: int, idLalana: int, idPk_debut: int, idPk_fin: int, niveau: int) -> None:
        self._idSimba = idSimba
        self._idLalana = idLalana
        self._idPk_debut = idPk_debut  # km
        self._idPk_fin  = idPk_fin     # km
        self._niveau = niveau

    def calc_cout(self, con, prix_metre_cube: float) -> float:
        return self.calc_volume(con) * prix_metre_cube

    def calc_volume(self, con) -> float:
        lalana = LalanaDAO.find_by_id(con, self._idLalana)
        pk_debut = PkDAO.find_by_id(con, self._idPk_debut)._valeur
        pk_fin = PkDAO.find_by_id(con, self._idPk_fin)._valeur

        longueur = (pk_fin - pk_debut) * 1000           # m
        profondeur = (self._niveau / 10)                # cm
        profondeur /= 100                               # m

        return longueur * profondeur * lalana._largeur  # m3

    def calc_duration(self, con, duree_metre_cube: float) -> float:
        return self.calc_volume(con) * duree_metre_cube
