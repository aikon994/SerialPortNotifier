@echo off
setlocal
title Build SerialPortNotifier

echo.
echo ==========================================
echo       SerialPortNotifier - Build EXE
echo ==========================================
echo.

py -m pip install --upgrade pip
py -m pip install -r requirements.txt
if errorlevel 1 goto error

py -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name SerialPortNotifier ^
  src\serial_port_notifier.py

if errorlevel 1 goto error

echo.
echo Build completed successfully.
echo EXE: dist\SerialPortNotifier.exe
echo.
pause
exit /b 0

:error
echo.
echo Build failed.
echo Verify that Python is installed and that "py" works.
pause
exit /b 1
