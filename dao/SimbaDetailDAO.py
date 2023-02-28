from connection.Bdd import Bdd

class SimbaDetailDAO:
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
                from simba_detail
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
    
    @staticmethod
    def find_simba_within_limit(con, point_couche, limit):
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select * from simba_detail
                where st_dwithin(coord_debut, %s, %s) or st_dwithin(coord_fin, %s, %s)
            """
            value = (point_couche, limit, point_couche, limit)
            cur.execute(sql, value)
            rep = cur.fetchall()

        except(Exception) as e:
            raise e
        finally:
            if __is_open:
                con.close()
            cur.close()
        return rep