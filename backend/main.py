from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    proje : str

class ListCreateRequest(BaseModel):
    name: str
lists = [
    {"id": 1, "name": "Alışveriş"},
    {"id": 2, "name": "Proje"},
]

@app.delete("/lists/{list_id}")
def delete_list(list_id: int):
    global lists
    for item in lists:
        if item["id"] == list_id:
            lists.remove(item)
            return {"message": f"List with id {list_id} deleted"}
    return {"error": "List not found"}
@app.post("/lists")
def create_list(request: ListCreateRequest):
    return { "id": 2, "name": request.name }

@app.get("/lists")
def read_root():
   return [
        { "id": 1, "name": "Alışveriş" },
        { "id": 2, "name": "Kitaplar" },
        { "id": 3, "name": "Yapılacaklar" }
    ]

@app.get("/lists/{list_id}/items")
def read_root():
   return [
        { "id": 1, "name": "...", "status": "PENDING"},
                { "id": 2, "name": "...", "status": "PENDING"}

    ]
@app.post("/lists/{list_id}/items")
def create_list():
   return [
       { "name": "...", "description": "...", "deadline": "2025-06-01", "status": "PENDING" }                                                        

    ]
@app.delete("/items/{item_id}")
def delete_list(item_id: int):
    global items
    for item in items:
        if items["id"] == item_id:
            lists.remove(item)
            return {"message": f"item with id {item_id} deleted"}
    return {"error": "Item not found"}