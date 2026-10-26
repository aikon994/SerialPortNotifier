# SerialPortNotifier for Windows 11

A tiny Windows 11 utility that monitors serial/COM ports and shows a popup whenever a USB-to-serial adapter is connected or disconnected.

## Features

- Detects newly connected and disconnected COM ports
- Shows a popup in the bottom-right corner
- Displays COM port, description, manufacturer, VID/PID and USB serial number
- Runs silently in the background
- Supports automatic startup at Windows login
- Supports common USB-serial adapters such as FTDI, CH340, CP210x and Prolific

## Build

```powershell
py -m pip install -r requirements.txt
build_exe.bat
```

The executable is created in:

```text
dist\SerialPortNotifier.exe
```

## Automatic startup

Run:

```text
install_autostart.bat
```

To remove automatic startup:

```text
remove_autostart.bat
```

## Run from source

```powershell
py src\serial_port_notifier.py
```
