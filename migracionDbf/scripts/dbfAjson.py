from dbfread import DBF
import json
from datetime import date

dbf_file = r"Z:/Bases/CLIENTES.dbf"  # Cambiá esta ruta

table = DBF(dbf_file, load=True, encoding='latin-1')

records = []
for record in table:
    cleaned = {
        key: str(value) if isinstance(value, date) else value
        for key, value in record.items()
    }
    records.append(cleaned)

with open("clientes.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4, ensure_ascii=False)

print("✔ Exportado como clientes.json")
