from connection.Bdd import Bdd
from dao.PkDAO import PkDAO

def main():
    con = Bdd.connect()
    data = PkDAO.find_all_pk_in_simba(con, 1)
    print(data)
    con.close()

if __name__ == "__main__":
    main()

# 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