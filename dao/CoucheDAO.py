from connection.Bdd import Bdd

class CoucheDAO:
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

    @staticmethod
    def find_all_couche_coord(con):
        __is_open = False
        try:
            if con is None:
                __is_open = True
                con = Bdd.connect()
            
            cur = con.cursor()
            sql = """
                select *, st_x(st_astext(coord)), st_y(st_astext(coord))
                from couche_coord
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