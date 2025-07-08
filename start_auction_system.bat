@echo off
echo ========================================
echo    Smart Auction AI System Startup
echo ========================================
echo.

echo Starting Backend Server...
start "Backend Server" cmd /k "python start_backend.py"

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak > nul

echo Starting Frontend...
start "Frontend" cmd /k "python start_frontend.py"

echo.
echo ========================================
echo    Services Started Successfully!
echo ========================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:8501
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to close this window...
pause > nul 