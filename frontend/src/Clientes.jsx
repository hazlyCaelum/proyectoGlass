// src/Clientes.jsx
import { useEffect, useState } from 'react'

function Clientes() {
  const [clientes, setClientes] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/clientes`) // 👈 tu IP local real
      .then((res) => {
        if (!res.ok) throw new Error('Error al cargar los clientes')
        return res.json()
      })
      .then((data) => {
        setClientes(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  if (loading) return <p>Cargando clientes...</p>
  if (error) return <p className="text-red-600">⚠️ {error}</p>

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Lista de Clientes</h2>
      <table className="w-full text-sm text-left border">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">Codigo</th>
            <th className="p-2 border">Nombre</th>
            <th className="p-2 border">CUIT</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map((cliente) => (
            <tr key={cliente.id} className="hover:bg-gray-50">
              <td className="p-2 border">{cliente.codigo}</td>
              <td className="p-2 border">{cliente.nombre}</td>
              <td className="p-2 border">{cliente.cuit}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Clientes
