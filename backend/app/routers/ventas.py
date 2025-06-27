from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List
import sqlite3

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)

DB_PATH = "app/ventas.db"

class Venta(BaseModel):
    ncompint: int
    ccomptip: str
    fecha: str
    cliente: str
    nombre: str
    codigo: str
    descripcion: str
    cantidad: float
    precio: float
    total: float
    grupo: str | None = ""
    clase: str | None = ""
    
def fetch_ventas(query: str, params: tuple = ()) -> List[Venta]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    ventas = []
    for i, row in enumerate(rows):
        try:
            v = dict(row)
            v["cantidad"] = float(v.get("cantidad") or 0.0)
            v["precio"] = float(v.get("precio") or 0.0)
            v["total"] = float(v.get("total") or 0.0)
            v["ncompint"] = int(v.get("ncompint") or 0)
            ventas.append(v)
        except Exception as e:
            print(f"❌ Error en fila {i} - {v.get('codigo', '???')}: {e}")
    return ventas



@router.get("/", response_model=List[Venta])
def listar_ventas():
    return fetch_ventas("SELECT * FROM ventas")

@router.get("/cliente/{codigo}", response_model=List[Venta])
def ventas_por_cliente(codigo: str):
    return fetch_ventas("SELECT * FROM ventas WHERE cliente = ?", (codigo,))

@router.get("/articulo/{codigo}", response_model=List[Venta])
def ventas_por_articulo(codigo: str):
    return fetch_ventas("SELECT * FROM ventas WHERE codigo = ?", (codigo,))

@router.get("/fecha/{fecha}", response_model=List[Venta])
def ventas_por_fecha(fecha: str):  # formato esperado: 'YYYY-MM-DD'
    return fetch_ventas("SELECT * FROM ventas WHERE fecha = ?", (fecha,))

@router.get("/rango-fechas/", response_model=List[Venta])
def ventas_por_rango_fechas(desde: str = Query(...), hasta: str = Query(...)):
    return fetch_ventas("SELECT * FROM ventas WHERE fecha BETWEEN ? AND ?", (desde, hasta))
