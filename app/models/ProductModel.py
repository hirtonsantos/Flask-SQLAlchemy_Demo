from app.configs.database import db
from sqlalchemy import Column, Integer, String, desc
from dataclasses import dataclass


@dataclass
class ProductModel(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = "Product_Model"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(244))
