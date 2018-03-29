from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# category class
class Category(Base):
    __tablename__ = 'category'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


# Items Class
class Items(Base):
    __tablename__ = 'items'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(10), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.category_id,
            'description': self.description,
            'price': self.price,
            'category_id': self.category_id,
            'category': self.category.name
        }


# creating Database
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
