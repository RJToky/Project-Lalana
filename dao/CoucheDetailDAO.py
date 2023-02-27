from connection.Bdd import Bdd

class CoucheDetailDAO:
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
                from couche_detail
            """
            cur.execute(sql)
            data = cur.fetchall()

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return data
    
    @staticmethod
    def find_by_id(con, id: int):
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *
                from couche_detail
                where idCouche = %s
            """
            value = (id, )
            cur.execute(sql, value)
            data = cur.fetchall()

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return data