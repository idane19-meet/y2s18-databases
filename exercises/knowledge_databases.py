from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,age,hobby):
    student_object = Knowledge(
        name=name,
        age=age,
        hobby=hobby)
	
    session.add(student_object)
    session.commit()

def query_all_articles():
	return session.query(Knowledge).all()

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	session.query(Knowledge).all().delete()
	session.commit()

def edit_article_rating():
	pass

add_article("idan", 16, 'ball')
delete_all_articles()
print(query_all_articles())
