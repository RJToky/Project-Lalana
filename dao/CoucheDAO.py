from connection.Bdd import Bdd
from model.Couche import Couche

class CoucheDAO:
    @staticmethod
    def find_by_id(con, id: int) -> Couche:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from couche
                where idCouche = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = Couche(data[0], data[1])

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep

    @staticmethod
    def find_all(con):
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from couche
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = Couche(row[0], row[1])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep