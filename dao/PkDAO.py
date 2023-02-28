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

            rep = Pk(data[0], data[1], data[2])

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep
