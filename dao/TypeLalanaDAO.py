from connection.Bdd import Bdd
from model.TypeLalana import TypeLalana

class TypeLalanaDAO:
    @staticmethod
    def find_by_id(con, id: int) -> TypeLalana:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from typeLalana
                where idTypeLalana = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = TypeLalana(data[0], data[1], data[2], data[3])

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
                from typeLalana
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = TypeLalana(row[0], row[1], row[2], row[3])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep