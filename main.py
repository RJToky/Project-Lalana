from connection.Bdd import Bdd
from dao.SimbaDetailDAO import SimbaDetailDAO
from dao.CoucheDetailDAO import CoucheDetailDAO

def main():
    con = Bdd.connect()
    
    con.close()

if __name__ == "__main__":
    main()

# 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