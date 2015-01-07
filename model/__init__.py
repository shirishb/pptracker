from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# establish a constraint naming convention.
# see http://docs.sqlalchemy.org/en/latest/core/constraints.html#configuring-constraint-naming-conventions
Base.metadata.naming_convention = {
        "pk": "pk_%(table_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ix": "ix_%(table_name)s_%(column_0_name)s"
}

PRIORITY_HIGH = 200
PRIORITY_MEDIUM = 100
PRIORITY_LOW = 50

# common constraint string patterns
CONSTRAINT_UNSIGNED_INTEGER = "{0} is null or ({0} >= 0)"
CONSTRAINT_PRIORITY = "priority >= 0 and priority <= 255"
CONSTRAINT_DATE_BEFORE = "{0} is null or ({0} <= date('now'))"
CONSTRAINT_DATE_AFTER = "{0} is null or ({0} > date('now'))"
CONSTRAINT_STRING_LOWER = "{0} == lower({0})"

def create_sessionmaker(dbname):
    engine = create_engine("sqlite:///%s" % dbname, echo=True)
    #engine = create_engine("postgresql://localhost:5432/%s" % dbname, echo=True)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    return session

