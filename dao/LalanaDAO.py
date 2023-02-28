from connection.Bdd import Bdd
from model.Lalana import Lalana

class LalanaDAO:
    @staticmethod
    def find_by_id(con, id: int) -> Lalana:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from lalana
                where idLalana = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = Lalana(data[0], data[1], data[2], data[3])

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
                from lalana
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = Lalana(row[0], row[1], row[2], row[3])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep