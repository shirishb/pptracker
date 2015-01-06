from sqlalchemy import Column, ForeignKey, func, create_engine
from sqlalchemy.types import String, Integer, Date, Enum
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


PRIORITY_HIGH=200
PRIORITY_MEDIUM=100
PRIORITY_LOW=50

PROJECT_TYPE = {
    "book": "",
    "coding" : "",
}

ACTIVITY_TYPE = {
    "pages" : "",
    "problems" : "",
    "http_url" : "link"
}

class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    tag = Column(String(40), unique=True, nullable=False)
    name = Column(String(80), nullable=False)
    date_started = Column(Date, default=func.date())
    date_finished = Column(Date)
    priority = Column(Integer, default=0)
    type = Column(Enum, Enum(PROJECT_TYPE.keys()), nullable=False)
    isbn = Column(String(15))
    activities = relationship("Activity", backref="project")

    def __repr__(self):
        print "Project(id=%d, tag='%s', name='%s', started=%s, priority=%d" % \
              (self.id, self.tag, self.name, self.date_started, self.priority)


class Activity(Base):
    __tablename__ = "activity"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    description = Column(String(80), nullable=False)
    date_started = Column(Date, default=func.date())
    date_finished = Column(Date)
    priority = Column(Integer, default=0)
    type = Column(Enum, Enum(ACTIVITY_TYPE.keys()))
    int_data = Column(Integer)
    string_data = Column(String(255))
    date_planned = Column(Date)
    estimated_days = Column(Integer)

    def __repr__(self):
        print "Activity(id=%d, project_id=%d, "

def create_sessionmaker(dbname):
    engine = create_engine("sqlite:///%s" % dbname, echo=True)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return session

if __name__ == "__main__":
    session = create_sessionmaker("test.db")
    s = session()

    p = Project()
    p.tag = "npa"
    p.name= "Non-Project Activities"
    p.priority = 0
    p.type=u'book'

    s.add(p)
    s.commit()
