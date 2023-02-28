from connection.Bdd import Bdd
from model.Pk import Pk

class PkDAO:
    @staticmethod
    def find_by_id(con, id: int) -> Pk:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from pk
                where idPk = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = Pk(data[0], data[1], data[2], data[3])

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
                from pk
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = Pk(row[0], row[1], row[2], row[3])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep
    
    @staticmethod
    def get_prix_metre_cube(con, id: int) -> float:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select t.prix
                from pk p
                join lalana l on p.idLalana = l.idLalana
                join typeLalana t on l.idTypeLalana = t.idTypeLalana
                where p.idPk = %s
            """
            value = (id, )
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
    
    @staticmethod
    def get_duree_metre_cube(con, id: int) -> float:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select t.duree
                from pk p
                join lalana l on p.idLalana = l.idLalana
                join typeLalana t on l.idTypeLalana = t.idTypeLalana
                where p.idPk = %s
            """
            value = (id, )
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