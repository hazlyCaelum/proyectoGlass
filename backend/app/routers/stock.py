from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

class Producto(BaseModel):
    id: int
    nombre: str
    cantidad: int
    precio_unitario: float

stock = []

@router.get("/")
def listar_stock():
    return stock

@router.get("/{producto_id}")
def obtener_producto(producto_id: int):
    producto = next((p for p in stock if p["id"] == producto_id), None)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/")
def agregar_producto(producto: Producto):
    stock.append(producto.dict())
    return {"mensaje": "Producto agregado", "producto": producto}

@router.put("/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):
    for i, p in enumerate(stock):
        if p["id"] == producto_id:
            stock[i] = producto.dict()
            return {"mensaje": "Producto actualizado", "producto": producto}
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):
    for i, p in enumerate(stock):
        if p["id"] == producto_id:
            eliminado = stock.pop(i)
            return {"mensaje": "Producto eliminado", "producto": eliminado}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
