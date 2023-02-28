from connection.Bdd import Bdd
from dao.SimbaDAO import SimbaDAO
from dao.LalanaDAO import LalanaDAO

def main():
    con = Bdd.connect()
    simba1 = SimbaDAO.find_by_id(con, 1)
    val = simba1.calc_cout(con, 123)
    print(val)
    con.close()

if __name__ == "__main__":
    main()

# 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