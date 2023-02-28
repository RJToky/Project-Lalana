from connection.Bdd import Bdd
from model.TypeCouche import TypeCouche

class TypeCoucheDAO:
    @staticmethod
    def find_by_id(con, id: int) -> TypeCouche:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from typeCouche
                where idTypeCouche = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = TypeCouche(data[0], data[1])

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
                from typeCouche
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = TypeCouche(row[0], row[1])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep