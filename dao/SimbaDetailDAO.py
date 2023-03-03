from connection.Bdd import Bdd
from model.SimbaDetail import SimbaDetail

class SimbaDetailDAO:
    @staticmethod
    def find_by_id(con, id: int) -> SimbaDetail:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from simbaDetail
                where idSimba = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = SimbaDetail(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])

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
                from simbaDetail
            """
            cur.execute(sql)
            data = cur.fetchall()

            rep = []
            for row in data:
                temp = SimbaDetail(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                rep.append(temp)

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep
