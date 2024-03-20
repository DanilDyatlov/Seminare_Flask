# Таблица заказов должна содержать следующие поля:
# id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.

from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    status: str


class Order(BaseModel):
    id: int
    user_id: int
    goods_id: int
    order_date: str