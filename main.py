from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDAO import SimbaDAO
from dao.LalanaDAO import LalanaDAO
from dao.LalanaDetailDao import LalanaDetailDAO

def main():
    con = Bdd.connect()
    lalana_detail = LalanaDetailDAO.find_by_id(con, 2)
    print(lalana_detail)
    con.close()

if __name__ == "__main__":
    main()

# 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