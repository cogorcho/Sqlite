from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# Global Variables
SQLITE                  = 'sqlite'

# Table Names
PROVINCIAS     = 'Provincia'
SECTORES       = 'Sector'

class DB:

    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }



    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname='../db/api.db'):

        dbtype = dbtype.lower()

        print(SQLITE)

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")
