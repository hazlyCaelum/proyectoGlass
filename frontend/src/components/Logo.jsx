// src/components/Logo.jsx
import logo from './assets/logo.png'

function Logo() {
  return (
    <div className="flex justify-center items-center mt-10">
      <img
        src={logo}
        alt="Logo Lumen Glass"
        className="w-48 h-auto"
      />
    </div>
  )
}

export default Logo

