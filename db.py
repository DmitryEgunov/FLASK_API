
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://user:12345@127.0.0.1:5431/an_ad')
Session = sessionmaker(bind=engine)


