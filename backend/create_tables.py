from app.database.base import Base
from app.database.connection import engine

# importing orm models so sqlalchemy registers them 
from app.models.issue import Issue

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__=="__main__":
    create_tables()