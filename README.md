<p align="center">
  <img src="assets/logo.svg" alt="SerialPortNotifier logo" width="150">
</p>

<h1 align="center">SerialPortNotifier</h1>

<p align="center">
  Lightweight USB serial / COM port connection notifier for Windows 11 and Linux.
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/aikon994/SerialPortNotifier" alt="Latest release">
  <img src="https://img.shields.io/github/license/aikon994/SerialPortNotifier" alt="License">
  <img src="https://img.shields.io/badge/Windows-11-0078D4" alt="Windows 11">
  <img src="https://img.shields.io/badge/Linux-supported-FCC624" alt="Linux">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB" alt="Python">
</p>

<p align="center">
  <a href="https://github.com/aikon994/SerialPortNotifier/releases/download/v1.0.0/SerialPortNotifier.exe"><strong>⬇ Download SerialPortNotifier.exe</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/aikon994/SerialPortNotifier/releases/latest">Latest release</a>
</p>

---

SerialPortNotifier runs quietly in the background and shows a popup whenever a USB serial device is connected or disconnected.

Typical devices include **FTDI**, **CH340**, **CP210x**, **Prolific**, Arduino boards and other serial adapters.

## ✨ Features

- Detects newly connected serial/COM ports
- Detects disconnected serial/COM ports
- Shows device name and assigned port
- Displays manufacturer, VID/PID and USB serial number when available
- Lightweight background operation
- Windows automatic startup support
- Linux desktop notifications with popup fallback
- Open source and MIT licensed

## 🪟 Windows 11

The Windows version monitors COM ports and displays a custom popup in the bottom-right corner.

### Quick start

Download the ready-to-run executable:

**[⬇ Download SerialPortNotifier.exe](https://github.com/aikon994/SerialPortNotifier/releases/download/v1.0.0/SerialPortNotifier.exe)**

Run it and you should immediately see a startup notification. After that, connect or disconnect a USB serial adapter.

Example:

```text
USB serial connected

Port: COM7
USB-SERIAL CH340
Manufacturer: wch.cn
VID:PID 1A86:7523
```

For source builds and Windows autostart instructions, see [`windows/README.md`](windows/README.md).

## 🐧 Linux

The Linux version monitors devices such as:

```text
/dev/ttyUSB0
/dev/ttyACM0
```

It uses native desktop notifications through `notify-send` when available, with a Tk popup fallback.

For installation and autostart instructions, see [`linux/README.md`](linux/README.md).

## ❤️ Support this project

If SerialPortNotifier is useful to you, you can support continued development through Stripe.

### One-time support

- [☕ €3 — Coffee](https://donate.stripe.com/4gM3co3Ec77rdRLgMJ83C00)
- [🚀 €5 — Supporter](https://donate.stripe.com/00w7sE3Ec2Rb6pjbsp83C01)
- [💙 €10 — Big Support](https://donate.stripe.com/14A00cb6E8bvfZTaol83C02)

### Monthly support

- [⭐ €2/month](https://buy.stripe.com/9B6aEQa2A9fz3d72VT83C03)
- [⭐ €5/month](https://buy.stripe.com/6oU28kdeMfDX7tnaol83C04)
- [⭐ €10/month](https://buy.stripe.com/5kQ8wI4Ig3Vf6pjeEB83C05)

Payments are securely processed by Stripe.

## 📁 Repository structure

```text
SerialPortNotifier/
├── assets/
│   └── logo.svg
├── windows/
│   ├── src/serial_port_notifier.py
│   ├── build_exe.bat
│   ├── install_autostart.bat
│   ├── remove_autostart.bat
│   ├── requirements.txt
│   └── README.md
├── linux/
│   ├── src/serial_port_notifier.py
│   ├── install.sh
│   ├── uninstall.sh
│   ├── run.sh
│   ├── serial-port-notifier.desktop
│   ├── requirements.txt
│   └── README.md
├── LICENSE
└── .gitignore
```

## 🛠 Build from source

### Windows

```powershell
cd windows
build_exe.bat
```

### Linux

```bash
cd linux
chmod +x run.sh
./run.sh
```

## 📦 Releases

The Windows executable is built automatically through GitHub Actions.

**Current release:** [v1.0.0](https://github.com/aikon994/SerialPortNotifier/releases/tag/v1.0.0)

## 📄 License

SerialPortNotifier is released under the **MIT License**.
