from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
Base = declarative_base()

class Park(Base):
    __tablename__ = 'parks'
    park_id = Column(Integer, primary_key=True)
    park_code = Column(String, unique=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)

class Camp(Base):
    __tablename__ = 'camps'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    park_code = Column(String, ForeignKey('parks.park_code'))
    state = Column(String)
    longitude = Column(Integer)
    latitude = Column(Integer)
    totalSites = Column(Integer)
    tentOnly = Column(Integer)
    electricalHookups = Column(Integer)
    showers = Column(String)
    dumpStation = Column(String)
    host = Column(String)
    potableWater = Column(String)
    firewoodForSale = Column(String)
    reservationUrl = Column(String)
    park = relationship("Park")

Base.metadata.create_all(engine)
