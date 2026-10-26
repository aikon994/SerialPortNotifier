@echo off
setlocal

set "APP=%~dp0dist\SerialPortNotifier.exe"

if not exist "%APP%" (
    echo ERROR: SerialPortNotifier.exe not found.
    echo Run build_exe.bat first.
    pause
    exit /b 1
)

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" ^
 /v "SerialPortNotifier" ^
 /t REG_SZ ^
 /d "\"%APP%\"" ^
 /f

if errorlevel 1 (
    echo.
    echo ERROR while enabling automatic startup.
) else (
    echo.
    echo Automatic startup enabled successfully.
    echo %APP%
)

pause
