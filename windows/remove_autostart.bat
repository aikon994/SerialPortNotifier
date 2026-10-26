@echo off
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" ^
 /v "SerialPortNotifier" /f

echo.
echo Automatic startup removed.
pause
