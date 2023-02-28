class Couche:
    def __init__(self, idCouche: int, idTypeCouche: int, coord: str, nbr: float, nom: str) -> None:
        self.idCouche = idCouche
        self.idTypeCouche = idTypeCouche
        self.coord = coord
        self.nbr = nbr
        self.nom = nom