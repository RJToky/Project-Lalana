from connection.Bdd import Bdd
from dao.CoucheDAO import CoucheDAO

def main():
    con = Bdd.connect()
    data = CoucheDAO.find_all_couche_coord(con)
    print(data)
    
    con.close()

if __name__ == "__main__":
    main()

# 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