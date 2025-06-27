import { useEffect, useState } from 'react'

function Clientes() {
  const [clientes, setClientes] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [busqueda, setBusqueda] = useState('')
  const [paginaActual, setPaginaActual] = useState(1)

  const clientesPorPagina = 10

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/clientes`)
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

  const clientesFiltrados = clientes.filter((cliente) =>
    cliente.codigo.toLowerCase().includes(busqueda.toLowerCase())
  )

  const totalPaginas = Math.ceil(clientesFiltrados.length / clientesPorPagina)
  const indiceInicio = (paginaActual - 1) * clientesPorPagina
  const clientesPagina = clientesFiltrados.slice(indiceInicio, indiceInicio + clientesPorPagina)

  const cambiarPagina = (nuevaPagina) => {
    if (nuevaPagina >= 1 && nuevaPagina <= totalPaginas) {
      setPaginaActual(nuevaPagina)
    }
  }

  const handleEliminar = (id) => {
    if (!confirm('¿Eliminar cliente?')) return
    fetch(`${import.meta.env.VITE_API_URL}/clientes/${id}`, { method: 'DELETE' })
      .then(() => setClientes((prev) => prev.filter((c) => c.id !== id)))
      .catch((err) => alert(`Error: ${err.message}`))
  }

  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-xl font-semibold mb-4 text-blue-700">📋 Lista de Clientes</h2>

      <input
        type="text"
        placeholder="🔎 Buscar por código..."
        className="mb-4 px-4 py-2 border rounded w-full shadow-sm"
        value={busqueda}
        onChange={(e) => {
          setBusqueda(e.target.value)
          setPaginaActual(1)
        }}
      />

      <div className="overflow-x-auto">
        <table className="w-full text-sm border rounded-lg">
          <thead className="bg-blue-50">
            <tr>
              <th className="p-2 border">Código</th>
              <th className="p-2 border">Nombre</th>
              <th className="p-2 border">CUIT</th>
              <th className="p-2 border">Acciones</th>
            </tr>
          </thead>
          <tbody>
            {clientesPagina.map((cliente) => (
              <tr key={cliente.id} className="hover:bg-gray-100 transition">
                <td className="p-2 border">{cliente.codigo}</td>
                <td className="p-2 border">{cliente.nombre}</td>
                <td className="p-2 border">{cliente.cuit}</td>
                <td className="p-2 border space-x-2">
                  <button className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-xs">
                    Editar
                  </button>
                  <button
                    onClick={() => handleEliminar(cliente.id)}
                    className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-xs"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
            {clientesPagina.length === 0 && (
              <tr>
                <td colSpan="4" className="text-center py-4 text-gray-500">
                  No se encontraron resultados.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <div className="flex justify-between items-center mt-4">
        <button
          onClick={() => cambiarPagina(paginaActual - 1)}
          disabled={paginaActual === 1}
          className="px-3 py-1 bg-gray-300 hover:bg-gray-400 rounded disabled:opacity-50"
        >
          ⬅️ Anterior
        </button>
        <span className="text-sm">Página {paginaActual} de {totalPaginas}</span>
        <button
          onClick={() => cambiarPagina(paginaActual + 1)}
          disabled={paginaActual === totalPaginas}
          className="px-3 py-1 bg-gray-300 hover:bg-gray-400 rounded disabled:opacity-50"
        >
          Siguiente ➡️
        </button>
      </div>
    </div>
  )
}

export default Clientes
