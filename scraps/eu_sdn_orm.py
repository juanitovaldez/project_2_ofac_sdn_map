from sqlalchemy import ForeignKey, Table, Column, Integer, Numeric, String, create_engine
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

db_path = r'C:\Users\Juan\bootcamp\projects\project_2\dbase\us_sdn.sqlite'
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()

class (Base):
    __tablename__ = 'SDN'
    ent_num   = Column(Integer(), primary_key=True)
    SDN_Name  = Column(String(350))
    SDN_Type  = Column(String(12))
    Program   = Column(String(200))
    Title     = Column(String(200))
    Call_Sign = Column(String(8))
    Vess_type = Column(String(25))
    Tonnage   = Column(String(14))
    GRT       = Column(String(8))
    Vess_flag = Column(String(40))
    Vess_owner= Column(String(150))
    Remarks   = Column(String(1000))
   
class ALT(Base):
    __tablename__ = 'alt'
    alt_num = Column(Integer(), primary_key=True)
    ent_num = Column(Integer(), ForeignKey(SDN.ent_num))
    alt_type = Column(String(8))
    alt_name = Column(String(300))
    alt_remarks = Column(String(250))
    ent = relationship("SDN", backref=backref("alt", order_by=ent_num))

class ADD(Base):
    __tablename__ = 'add'
    add_num = Column(Integer(), primary_key=True)
    ent_num = Column(Integer(), ForeignKey(SDN.ent_num))
    adress = Column(String(750))
    csppc = Column(String(116))
    country = Column(String(250))
    add_remarks = Column(String(200))
    ent = relationship("SDN", backref=backref("add", order_by=ent_num))

class COMMENTS(Base):
    __tablename__ = 'sdn_comments'
    ent_num = Column(Integer(), ForeignKey(SDN.ent_num), primary_key=True)
    remarks_extended = Column(String())
    ent = relationship("SDN", uselist=False)


Base.metadata.create_all(engine)