from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO
from dao.SimbaDAO import SimbaDAO

def main():
    con = Bdd.connect()
    simba = SimbaDAO.find_by_id(con, 1)
    cout = simba.calc_cout(con)
    print("Cout = ", cout)
    con.close()

if __name__ == "__main__":
    main()

# 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