from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
from datetime import date

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

DB_PATH = "app/pedidos.db"

class PedidoDetalle(BaseModel):
    codigo: str
    descripcion: str | None = None
    cantidad: float
    precio: float
    total: float

class Pedido(BaseModel):
    cliente: str
    fecha: str = date.today().isoformat()
    tipo: str = "PED"
    observaciones: str | None = None
    detalles: List[PedidoDetalle]

class PedidoRespuesta(Pedido):
    id: int

@router.post("/", response_model=PedidoRespuesta)
def crear_pedido(pedido: Pedido):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insertar en encabezado
    cursor.execute("""
        INSERT INTO pedidos (cliente, fecha, tipo, observaciones)
        VALUES (?, ?, ?, ?)
    """, (pedido.cliente, pedido.fecha, pedido.tipo, pedido.observaciones))
    pedido_id = cursor.lastrowid

    # Insertar cada línea
    for item in pedido.detalles:
        cursor.execute("""
            INSERT INTO pedido_detalle (pedido_id, codigo, descripcion, cantidad, precio, total)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            pedido_id,
            item.codigo,
            item.descripcion or "",
            item.cantidad,
            item.precio,
            item.total
        ))

    conn.commit()
    conn.close()

    return PedidoRespuesta(id=pedido_id, **pedido.dict())

@router.get("/{pedido_id}", response_model=Pedido)
def obtener_pedido(pedido_id: int):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
    encabezado = cursor.fetchone()
    if not encabezado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    cursor.execute("SELECT * FROM pedido_detalle WHERE pedido_id = ?", (pedido_id,))
    detalles = cursor.fetchall()

    conn.close()

    return Pedido(
        cliente=encabezado["cliente"],
        fecha=encabezado["fecha"],
        tipo=encabezado["tipo"],
        observaciones=encabezado["observaciones"],
        detalles=[{
            "codigo": d["codigo"],
            "descripcion": d["descripcion"],
            "cantidad": d["cantidad"],
            "precio": d["precio"],
            "total": d["total"]
        } for d in detalles]
    )

@router.get("/", response_model=List[PedidoRespuesta])
def listar_pedidos():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    return [PedidoRespuesta(
        id=row["id"],
        cliente=row["cliente"],
        fecha=row["fecha"],
        tipo=row["tipo"],
        observaciones=row["observaciones"],
        detalles=[]  # No se listan detalles aquí
    ) for row in rows]
