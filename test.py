from model import create_sessionmaker
from model.project import Project
from model.activity import Activity


if __name__ == "__main__":
    session = create_sessionmaker(":memory:")
    s = session()

    p = Project("tilt", "Things I Learnt Today", 255)
    p.type= "book"
    print p
    s.add(p)
    s.commit()
    p = Project("npa", "Non-Project Activities", 0)
    p.type= "book"
    print p
    s.add(p)
    s.commit()
    s.close()

