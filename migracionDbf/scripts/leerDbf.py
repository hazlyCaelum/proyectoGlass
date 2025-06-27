import json
from dbfread import DBF
from datetime import date

# Ruta al archivo DBF
dbf_file = "C:/Users/sgclu/OneDrive/Escritorio/Proyecto WebApp Glass/Bases DBF/Bases/ARTICULO.dbf"

# Leer la tabla
table = DBF(dbf_file, load=True, encoding='latin-1')

# Convertir a lista de diccionarios con fechas como strings
records = []
for record in table:
    clean_record = {
        key: str(value) if isinstance(value, date) else value
        for key, value in record.items()
    }
    records.append(clean_record)

# Guardar como JSON
with open("articulos.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4, ensure_ascii=False)
