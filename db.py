from application import db
from films.models import Film

db.create_all()

film1 = Film("foo1", 1991, "bar1", "https://www.youtube.com/watch?v=ZrdQSAX2kyw&ab_channel=HBOMax")
film2 = Film("foo2", 2055, "bar2", "")
film3 = Film("foo3", 2001, "bar3", "")
film4 = Film("foo4", 1890, "bar4", "")

db.session.add_all([film1, film2, film3, film4])
db.session.commit()