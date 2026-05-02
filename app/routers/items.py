from fastapi import APIRouter, HTTPException, Path, Query
from app.schemas import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])
fake_db = {}
counter = 0


@router.post(
    "/",
    response_model=Item,
    summary="Создать новый товар",
    description="Создаёт новый товар с автоматически сгенерированным ID",
    response_description="Созданный товар с ID",
    responses={
        400: {"description": "Некорректные данные товара"}
    }
)
async def create_item(item: ItemCreate):
    global counter
    counter += 1
    new_item = Item(id=counter, **item.model_dump())
    fake_db[counter] = new_item
    return new_item


@router.get(
    "/{item_id}",
    response_model=Item,
    summary="Получить товар по ID",
    description="Возвращает информацию о товаре по его уникальному идентификатору",
    response_description="Информация о товаре"
)
async def get_item(
        item_id: int = Path(..., title="ID товара", description="Уникальный идентификатор товара", ge=1),
        q: str = Query(None, title="Поисковый запрос", description="Необязательный поисковый запрос")
):
    if item_id not in fake_db:
        raise HTTPException(404, "Item not found")
    return fake_db[item_id]