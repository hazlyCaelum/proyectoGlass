import { Outlet } from 'react-router-dom'

function Layout() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800">
      <header className="bg-white shadow-md py-4 px-6 mb-6">
        <h1 className="text-2xl font-bold text-blue-600">GlassApp - Gestión de Clientes</h1>
      </header>
      <main className="px-4 md:px-10">
        <Outlet />
      </main>
    </div>
  )
}

export default Layout
