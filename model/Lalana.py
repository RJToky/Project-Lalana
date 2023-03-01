from connection.Bdd import Bdd

class Lalana:
    def __init__(self, idLalana: int, nomLalana: str, largeur: float, idTypeLalana: int) -> None:
        self.idLalana = idLalana
        self.nomLalana = nomLalana
        self.largeur = largeur
        self.idTypeLalana = idTypeLalana

    def calc_cout_rn(self, con) -> float:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from calc_cout_rn(%s)
            """
            value = (self.idLalana, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = data[0]

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep