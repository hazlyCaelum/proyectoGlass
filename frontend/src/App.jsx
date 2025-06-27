// App.jsx
import { useState } from 'react'
import Clientes from './Clientes' // 👈 asegurate de que esté bien la ruta


function App() {
  const [view, setView] = useState('clientes')

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navbar */}
      <header className="bg-white shadow-md p-4">
        <div className="max-w-6xl mx-auto flex justify-between items-center">
          <h1 className="text-xl font-bold text-gray-800">Gestión de Ventas</h1>
          <div className="space-x-2">
            <button
              onClick={() => setView('clientes')}
              className={`px-4 py-2 rounded-md text-sm font-medium transition ${
                view === 'clientes'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              Clientes
            </button>
            <button
              onClick={() => setView('productos')}
              className={`px-4 py-2 rounded-md text-sm font-medium transition ${
                view === 'productos'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              Productos
            </button>
            <button
              onClick={() => setView('pedidos')}
              className={`px-4 py-2 rounded-md text-sm font-medium transition ${
                view === 'pedidos'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              Pedidos
            </button>
          </div>
        </div>
      </header>

      {/* Contenido */}
      <main className="max-w-6xl mx-auto px-4 py-8">
        <div className="bg-white shadow-md rounded-lg p-6">
          {view === 'clientes' && <Clientes />}
          {view === 'productos' && <p>📦 Aquí irá el catálogo de productos</p>}
          {view === 'pedidos' && <p>📝 Aquí irá la gestión de pedidos</p>}
        </div>
      </main>
    </div>
  )
}

export default App
