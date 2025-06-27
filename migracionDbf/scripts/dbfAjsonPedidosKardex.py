from dbfread import DBF
import json
from datetime import date, timedelta

# Ruta al archivo DBF
dbf_file = "Z:/BASES/KARDEX.dbf"  # ← Cambiá esta ruta

# Cargar tabla
table = DBF(dbf_file, load=True, encoding='latin-1')

# Fecha de corte: hace 1 años
hoy = date.today()
dos_anios_atras = hoy - timedelta(days=365)

# Nombre del campo de fecha (ajustalo si es distinto)
CAMPO_FECHA = "FECHA"  # ← Asegurate de que este sea el nombre correcto

# Filtrar y procesar
records = []
for record in table:
    fecha = record.get(CAMPO_FECHA)
    if isinstance(fecha, date) and fecha >= dos_anios_atras:
        cleaned = {
            key: str(value) if isinstance(value, date) else value
            for key, value in record.items()
        }
        records.append(cleaned)

# Guardar como JSON
with open("pedidos_ultimos2anios.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4, ensure_ascii=False)

print(f"✔ Exportados {len(records)} pedidos recientes a pedidos_ultimos2anios.json")
