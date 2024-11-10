from fastapi import APIRouter
from src.models.itemsModel import Item
from src.utils.jsonCustomResponse import jsonCustomResponse

router = APIRouter()

items = []

@router.get("/items/")
async def read_items():
    return jsonCustomResponse(200, "Items fetched successfully", items)

@router.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return jsonCustomResponse(201, "Item created successfully", item)

@router.post("/items/bulk")
async def create_items(items: list[Item]):
    for item in items:
        items.append(item)
    return jsonCustomResponse(201, "Items created successfully", items)

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return jsonCustomResponse(200, "Item fetched successfully", items[item_id])

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return jsonCustomResponse(200, "Item updated successfully", item)

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    return jsonCustomResponse(200, "Item deleted successfully", {})

