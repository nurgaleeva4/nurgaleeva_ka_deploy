from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(..., title="Название товара", description="Наименование товара", example="Ноутбук")
    price: float = Field(..., title="Цена", description="Цена товара в рублях", example=49999.99, gt=0)

class Item(ItemCreate):
    id: int = Field(..., title="ID товара", description="Уникальный идентификатор товара", example=1)