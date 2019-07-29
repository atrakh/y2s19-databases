from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

def add_article(artical_name, topic, rating):
        session = DBSession()
        artical_object=Knowledge(
                artical_name=artical_name,
                topic=topic,
                rating=rating)
        session.add(artical_object)
        session.commit()
        session.close()

def query_all_articles():
        session = DBSession()
        articals=session.query(Knowledge).all()
        session.close()
        return articals

def query_article_by_topic(their_topic):
	atical=session.query(Knowledge).filter_by(topic=their_topic).first()
	return atical


def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()

def edit_article_rating(artical_name,rating):
	artical_object=session.query(Knowledge).filter_by(artical_name=artical_name).first()
	artical_object.rating=rating
	session.commit()
