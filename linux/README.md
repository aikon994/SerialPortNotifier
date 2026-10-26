# SerialPortNotifier for Linux

A small Linux desktop utility that detects USB serial ports and shows a notification when a serial device is connected or disconnected.

Designed for Debian, Ubuntu, Linux Mint and similar desktop distributions.

## Features

- Detects `/dev/ttyUSB*`
- Detects `/dev/ttyACM*`
- Detects serial devices exposed by pyserial
- Shows connect/disconnect notifications
- Displays device path, description, manufacturer, VID/PID and USB serial number
- Uses native Linux notifications through `notify-send`
- Falls back to a Tk popup
- Can start automatically at desktop login

## Requirements

```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk libnotify-bin
python3 -m pip install --user -r requirements.txt
```

## Quick test

```bash
chmod +x run.sh
./run.sh
```

## Install

```bash
chmod +x install.sh
./install.sh
```

## Serial port permissions

```bash
sudo usermod -aG dialout $USER
```

Then log out and back in.
