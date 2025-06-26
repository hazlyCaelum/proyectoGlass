from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import clientes, pedidos, stock, articulos, ventas

app = FastAPI(
    title="GlassLab API",
    description="API para la gestión de frascos de vidrio",
    version="1.0.0"
)

# Permitir frontend local y otros orígenes si se expande en LAN
origins = [
    "http://localhost:5173",  # React local
    "http://192.168.1.100",   # IP del servidor local (LAN)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas base
app.include_router(clientes.router)
app.include_router(pedidos.router)
app.include_router(stock.router)
app.include_router(articulos.router)
app.include_router(ventas.router)
app.include_router(pedidos.router)


@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de GlassLab"}
