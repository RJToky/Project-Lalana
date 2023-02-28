from connection.Bdd import Bdd
from model.Simba import Simba

class SimbaDAO:
    @staticmethod
    def find_by_id(con, id: int) -> Simba:
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from simba
                where idSimba = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchone()

            rep = Simba(data[0], data[1], data[2], data[3])

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep
