# SerialPortNotifier

SerialPortNotifier is a lightweight utility that shows a desktop notification when a USB serial/COM device is connected or disconnected.

The project includes native-ready versions for **Windows 11** and **Linux desktop systems**.

## Platforms

### Windows 11

The Windows version monitors COM ports and shows a custom popup with:

- COM port number
- device description
- manufacturer
- VID/PID
- USB serial number when available
- connection and disconnection events
- automatic startup through the current-user Windows registry

See [`windows/README.md`](windows/README.md).

### Linux

The Linux version monitors serial devices such as `/dev/ttyUSB0` and `/dev/ttyACM0` and shows notifications through `notify-send`, with a Tk popup fallback.

It supports automatic startup using a `.desktop` file in `~/.config/autostart`.

See [`linux/README.md`](linux/README.md).

## Repository structure

```text
SerialPortNotifier/
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

## License

MIT License.
