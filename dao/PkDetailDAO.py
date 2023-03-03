from connection.Bdd import Bdd
from model.PkDetail import PkDetail

class PkDetailDAO:
    @staticmethod
    def find_by_id(con, id: int) -> PkDetail:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from pkDetail
                where idPk = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = PkDetail(data[0], data[1], data[2], data[3], data[4], data[5])

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
                from pkDetail
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = PkDetail(row[0], row[1], row[2], row[3], row[4], row[5])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep