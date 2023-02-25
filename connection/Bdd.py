import psycopg2

class Bdd:
    @staticmethod
    def connect():
        try:
            con = psycopg2.connect(
                host = "localhost",
                port = "5432",
                dbname = "lalana",
                user = "postgres",
                password = "root"
            )
        except(Exception, psycopg2.Error) as error:
            raise error
        return con