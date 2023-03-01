from connection.Bdd import Bdd
from dao.PkDAO import PkDAO
from dao.CoucheDetailDAO import CoucheDetailDAO

def main():
    con = Bdd.connect()
    data = CoucheDetailDAO.find_couche_in_lalana(con, 7, 1000)
    print(data)
    con.close()

if __name__ == "__main__":
    main()

# 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