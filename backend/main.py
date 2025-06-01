from typing import Union, List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için prod ortamında sadece frontend URL'si yazılır
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Veri modelleri
class ListCreateRequest(BaseModel):
    name: str

class ItemCreateRequest(BaseModel):
    name: str
    description: str
    deadline: str
    status: str  # "PENDING" ya da "DONE"

# Örnek veriler (RAM'de tutuluyor)
lists = [
    {"id": 1, "name": "Alışveriş"},
    {"id": 2, "name": "Proje"},
    {"id": 3, "name": "Okunacak Kitaplar"},
]

items = [
    {"id": 1, "list_id": 1, "name": "Süt al", "description": "1 litre süt al", "deadline": "2025-06-01", "status": "PENDING"},
    {"id": 2, "list_id": 1, "name": "Ekmek al", "description": "Taze ekmek al", "deadline": "2025-06-01", "status": "DONE"},
    {"id": 3, "list_id": 2, "name": "Sunum hazırla", "description": "PowerPoint hazırla", "deadline": "2025-06-03", "status": "PENDING"},
        {"id": 4, "list_id": 3, "name": "Sunum hazırla", "description": "PowerPoint hazırla", "deadline": "2025-06-03", "status": "PENDING"},

]

# Tüm listeleri getir
@app.get("/lists")
def get_lists():
    return lists

# Listeye ait görevleri getir
@app.get("/lists/{list_id}/items")
def get_items_by_list(list_id: int):
    return [item for item in items if item["list_id"] == list_id]

# Yeni liste oluştur
@app.post("/lists")
def create_list(request: ListCreateRequest):
    new_id = max([l["id"] for l in lists]) + 1 if lists else 1
    new_list = {"id": new_id, "name": request.name}
    lists.append(new_list)
    return new_list

# Liste sil
@app.delete("/lists/{list_id}")
def delete_list(list_id: int):
    global lists, items
    lists = [l for l in lists if l["id"] != list_id]
    items = [i for i in items if i["list_id"] != list_id]
    return {"message": f"List with id {list_id} and its items deleted"}

# Yeni görev oluştur
@app.post("/lists/{list_id}/items")
def create_item(list_id: int, request: ItemCreateRequest):
    new_id = max([i["id"] for i in items]) + 1 if items else 1
    new_item = {
        "id": new_id,
        "list_id": list_id,
        "name": request.name,
        "description": request.description,
        "deadline": request.deadline,
        "status": request.status
    }
    items.append(new_item)
    return new_item

# Görev sil
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"message": f"Item with id {item_id} deleted"}
    return {"error": "Item not found"}
