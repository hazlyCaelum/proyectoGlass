import { useEffect, useState } from 'react'

function Articulos() {
  const [articulos, setArticulos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [busqueda, setBusqueda] = useState('')
  const [paginaActual, setPaginaActual] = useState(1)
  const articulosPorPagina = 10

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/articulos`)
      .then((res) => {
        if (!res.ok) throw new Error('Error al cargar los artículos')
        return res.json()
      })
      .then((data) => {
        setArticulos(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  const articulosFiltrados = articulos.filter((art) =>
    art.descripcion.toLowerCase().includes(busqueda.toLowerCase()) ||
    art.codigo.toLowerCase().includes(busqueda.toLowerCase())
  )

  const totalPaginas = Math.ceil(articulosFiltrados.length / articulosPorPagina)
  const indiceInicial = (paginaActual - 1) * articulosPorPagina
  const articulosPaginados = articulosFiltrados.slice(indiceInicial, indiceInicial + articulosPorPagina)

  const cambiarPagina = (nuevaPagina) => {
    if (nuevaPagina >= 1 && nuevaPagina <= totalPaginas) {
      setPaginaActual(nuevaPagina)
    }
  }

  if (loading) return <p>Cargando artículos...</p>
  if (error) return <p className="text-red-600">⚠️ {error}</p>

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Lista de Artículos</h2>

      <input
        type="text"
        placeholder="Buscar por código o descripción..."
        className="mb-4 px-3 py-2 border rounded w-full shadow"
        value={busqueda}
        onChange={(e) => {
          setBusqueda(e.target.value)
          setPaginaActual(1) // Reinicia a la primera página si cambia la búsqueda
        }}
      />

      <table className="w-full text-sm text-left border">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">Código</th>
            <th className="p-2 border">Descripción</th>
            <th className="p-2 border">Unidad</th>
            <th className="p-2 border">Precio</th>
          </tr>
        </thead>
        <tbody>
          {articulosPaginados.map((art) => (
            <tr key={art.id} className="hover:bg-gray-50">
              <td className="p-2 border">{art.codigo}</td>
              <td className="p-2 border">{art.descripcion}</td>
              <td className="p-2 border">{art.unidad}</td>
              <td className="p-2 border">{art.precio}</td>
            </tr>
          ))}
          {articulosPaginados.length === 0 && (
            <tr>
              <td colSpan="4" className="p-4 text-center text-gray-500">
                No se encontraron artículos
              </td>
            </tr>
          )}
        </tbody>
      </table>

      {/* Controles de paginación */}
      {totalPaginas > 1 && (
        <div className="flex justify-center items-center mt-4 space-x-2">
          <button
            onClick={() => cambiarPagina(paginaActual - 1)}
            disabled={paginaActual === 1}
            className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
          >
            ◀
          </button>
          <span className="text-sm text-gray-600">
            Página {paginaActual} de {totalPaginas}
          </span>
          <button
            onClick={() => cambiarPagina(paginaActual + 1)}
            disabled={paginaActual === totalPaginas}
            className="px-3 py-1 bg-gray-200 rounded disabled:opacity-50"
          >
            ▶
          </button>
        </div>
      )}
    </div>
  )
}

export default Articulos
