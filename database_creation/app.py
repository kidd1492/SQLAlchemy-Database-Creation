from models import Park, engine, Camp
from sqlalchemy.orm import sessionmaker
import pandas as pd

Session = sessionmaker(bind=engine)

session = Session()

df = pd.read_csv("database_creation/NPSparks.csv")
df_camps = pd.read_csv("database_creation/NPSCamps.csv")

for index, row in df.iterrows():
    park = Park(
        park_id=row['park_id'],
        park_code=row['park_code'],
        name=row['name'],
        description=row['description'],
        url=row['url']
    )
    session.add(park)

# Commit changes to the database
session.commit()

for index, row in df_camps.iterrows():
    camp = Camp(
        name=row['name'],
        park_code=row['parkCode'],
        state=row['state'],
        longitude=row['longitude'],
        latitude=row['latitude'],
        totalSites=row['totalSites'],
        tentOnly=row['tentOnly'],
        electricalHookups=row['electricalHookups'],
        showers=row['showers'],
        dumpStation=row['dumpStation'],
        host=row['host'],
        potableWater=row['potableWater'],
        firewoodForSale=row['firewoodForSale'],
        reservationUrl=row['reservationUrl']
    )
    session.add(camp)

# Commit changes to the database after the loop
session.commit()