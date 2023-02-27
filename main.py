import json
from connection.Bdd import Bdd
from dao.CoucheDetailDAO import CoucheDetailDAO

def main():
    con = Bdd.connect()
    data = CoucheDetailDAO.find_by_id(None, 0)
    # data = [2, 3, 4]
    d = json.dumps(data)
    print(data)
    
    con.close()

if __name__ == "__main__":
    main()

# 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