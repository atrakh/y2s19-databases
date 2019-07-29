from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
        __tablename__='articals'
        artical_id=Column(Integer, primary_key=True)
        artical_name= Column(String)
        topic=Column(String)
        rating=Column(Integer)
        def __repr__(self):
                return ("artica name: {}\n"
                        "artical topic: {}\n"
                        "rating:{}").format(
                                self.artical_name,
                                self.topic,
                                self.rating)
a=Knowledge(artical_name="bla", topic="bla bla", rating=10)
print (a)
