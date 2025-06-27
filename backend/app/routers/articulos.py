from fastapi import APIRouter, HTTPException
import sqlite3
from typing import List
from pydantic import BaseModel

router = APIRouter(
    prefix="/articulos",
    tags=["Artículos"]
)

# Modelo Pydantic para respuestas
class Articulo(BaseModel):
    codigo: str
    descripcion: str
    descripcion_etiqueta: str
    grupo: str
    embalaje: float
    stock_minimo: int
    costo: float
    precio: float
    activo: bool
    lstock: bool
    iva: int
    barra: str
    tipo: str
    fecha_creacion: str | None

DB_PATH = "app/articulos.db" # Ruta local al archivo SQLite

@router.get("/", response_model=List[Articulo])
def listar_articulos():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articulos")
        rows = cursor.fetchall()
        conn.close()

        articulos = []
        for row in rows:
            clean = dict(row)
            clean["descripcion"] = clean["descripcion"] or ""
            clean["descripcion_etiqueta"] = clean["descripcion_etiqueta"] or ""
            clean["grupo"] = clean["grupo"] or ""
            clean["barra"] = clean["barra"] or ""
            clean["fecha_creacion"] = clean["fecha_creacion"] or None
            clean["activo"] = bool(clean["activo"])
            clean["lstock"] = bool(clean["lstock"])
            clean["costo"] = float(clean["costo"] or 0.0)
            clean["precio"] = float(clean["precio"] or 0.0)
            articulos.append(clean)

        return articulos

    except Exception as e:
        print(f"💥 Error general en la consulta de artículos: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})



@router.get("/{codigo}", response_model=Articulo)
def obtener_articulo(codigo: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articulos WHERE codigo = ?", (codigo,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="Artículo no encontrado")
