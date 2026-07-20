from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:12345678@localhost:3306/campus_core"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)