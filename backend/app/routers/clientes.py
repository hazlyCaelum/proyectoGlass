from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

DB_PATH = "app/clientes.db"

class Cliente(BaseModel):
    codigo: str
    nombre: str
    cuit: str
    direccion: str | None = None
    localidad: str | None = None
    email: str | None = None
    telefono: str | None = None
    celular: str | None = None
    activo: bool

@router.get("/", response_model=List[Cliente])
def listar_clientes():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    conn.close()

    clientes = []
    for row in rows:
        cliente = dict(row)
        cliente["activo"] = bool(cliente["activo"])
        clientes.append(cliente)

    return clientes

@router.get("/{codigo}", response_model=Cliente)
def obtener_cliente(codigo: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE codigo = ?", (codigo,))
    row = cursor.fetchone()
    conn.close()
    if row:
        cliente = dict(row)
        cliente["activo"] = bool(cliente["activo"])
        return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

