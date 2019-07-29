from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(artical_name, topic, rating):
        artical_object=Knowledge(
                artical_name=artical_name,
                topic=topic,
                rating=rating)
        session.add(artical_object)
        session.commit()
add_article("pizza", "food", 10)
add_article("burger", "food", 8)
add_article("fish", "animal", 7)
add_article("dog", "animal", 5)
add_article("almog", "name", 10)
	

def query_all_articles():
	articals=session.query(Knowledge).all()
	return articals
print(query_all_articles())	

def query_article_by_topic(their_topic):
	atical=session.query(Knowledge).filter_by(topic=their_topic).first()
	return atical
print(query_article_by_topic("food"))


def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()
delete_article_by_topic("food")

def delete_all_articles():
	session.query(Knowledge).delete()
delete_all_articles()


	

def edit_article_rating(artical_name,rating):
	artical_object=session.query(Knowledge).filter_by(artical_name=artical_name).first()
	artical_object.rating=rating
	session.commit()
edit_article_rating("dog", 10)
	
