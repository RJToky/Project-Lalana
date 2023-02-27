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
                select cc.idCouche_coord, c.karazany, st_x(st_astext(cc.coord)), st_y(st_astext(cc.coord)), cc.nom
                from couche c
                natural join couche_coord cc
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