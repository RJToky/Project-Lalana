from connection.Bdd import Bdd

class SimbaDAO:
    @staticmethod
    def find_pk_debut_fin(con):
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
            rep = cur.fetchall()

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep