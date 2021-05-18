from sqlalchemy import create_engine,Column,Boolean,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import time as tm
engine=create_engine('sqlite:///prisp.db',connect_args={'check_same_thread':False})
Base=declarative_base()

class _Prispevok(Base):
    __tablename__='prisp'
    
    id=Column(Integer,primary_key=True)
    uname=Column(String)
    time=Column(String)
    text=Column(String)
class Prispevok:
    def __init__(self,uname,time,text):
        p=_Prispevok(uname=uname,time=time,text=text)
        session.add(p)
        session.commit()
        tm.sleep(0.01)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
def by_uname(uname):
    return session.query(_Prispevok).filter(_Prispevok.uname==uname)[0]
def all_p(isl=False):
    try:
        tm.sleep(0.01)
        return session.query(_Prispevok).all()
    except sqlalchemy.exc.InvalidRequestError:
        raise
