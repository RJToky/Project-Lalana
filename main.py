from connection.Bdd import Bdd
from dao.SimbaDAO import SimbaDAO
from dao.LalanaDAO import LalanaDAO
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.LalanaDetailDao import LalanaDetailDAO
from dao.SimbaDetailDAO import SimbaDetailDAO
from model.Lalana import Lalana

def main():
    con = Bdd.connect()
    data = LalanaDetailDAO.find_by_id(con, 7)
    print(data.dureeReparation)
    con.close()

if __name__ == "__main__":
    main()

# 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