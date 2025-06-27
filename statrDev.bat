@echo off
setlocal enabledelayedexpansion

echo === Iniciando servidores de desarrollo ===

:: Rutas relativas
set BACKEND_DIR=backend
set FRONTEND_DIR=frontend
set VENV_DIR=%BACKEND_DIR%\venv
set LOG_DIR=logs

:: Crear carpeta de logs si no existe
if not exist %LOG_DIR% (
    mkdir %LOG_DIR%
)

:: Verificar entorno virtual
if not exist %VENV_DIR%\Scripts\activate.bat (
    echo [ERROR] No se encontró el entorno virtual en %VENV_DIR%
    pause
    exit /b
)

:: Activar entorno virtual y lanzar backend
echo Iniciando backend...
start cmd /k "cd /d %BACKEND_DIR% && call venv\Scripts\activate.bat && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

:: Iniciar frontend
echo Iniciando frontend...
start cmd /k "cd /d %FRONTEND_DIR% && npm run dev -- --host 0.0.0.0"

echo Servidores iniciados en terminales separadas.
echo.
pause
