// src/components/LogoAnimado.jsx
import { motion } from 'framer-motion'
import logo from './assets/logo.png' // usa la ruta real si es diferente

function LogoAnimado() {
  return (
    <div className="flex justify-center items-center h-[60vh] bg-white">
      <motion.img
        src={logo}
        alt="Logo Lumen Glass SRL"
        className="w-48 h-48 object-contain"
        initial={{ rotate: 0, opacity: 0 }}
        animate={{ rotate: 360, opacity: 1 }}
        transition={{
          duration: 2,
          ease: 'easeInOut',
          repeat: Infinity,
          repeatType: 'loop',
        }}
      />
    </div>
  )
}

export default LogoAnimado
