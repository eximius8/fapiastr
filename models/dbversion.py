from sqlalchemy import  Column, Integer
from dbutils.dbconnect import Base, loadSession

class Versiondb(Base):
    
    @classmethod
    def increm(cls, val):
        session = loadSession()
        vsn = session.query(cls).all()        
        vsn[0].db = vsn[0].db + val
        newver = int(vsn[0].db)      
        session.commit()
        session.close()
        return newver
        
    @classmethod
    def get_version(cls):
        session = loadSession()
        #session.expunge_all()
        qry = session.query(cls).all()
        vsn = int(qry[0].db)        
        session.close()
        return vsn
    
    db = Column('DB', Integer, primary_key=True)
    __tablename__ = 'Version'