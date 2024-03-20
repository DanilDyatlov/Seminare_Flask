# Таблица товаров должна содержать следующие поля:
# id (PRIMARY KEY), название, описание и цена.
from pydantic import BaseModel, Field


class GoodsIn(BaseModel):
    name: str
    description: str = Field(max_length=256)
    price: int


class Goods(BaseModel):
    id: int
    name: str
    description: str = Field(max_length=256)
    price: int