#!/usr/bin/env bash
set -e

APP_DIR="$HOME/.local/share/serial-port-notifier"
BIN_DIR="$HOME/.local/bin"
AUTOSTART_DIR="$HOME/.config/autostart"

echo "Installing SerialPortNotifier..."

mkdir -p "$APP_DIR" "$BIN_DIR" "$AUTOSTART_DIR"

python3 -m pip install --user -r requirements.txt

cp src/serial_port_notifier.py "$APP_DIR/serial_port_notifier.py"
chmod +x "$APP_DIR/serial_port_notifier.py"

cat > "$BIN_DIR/serial-port-notifier" <<EOF
#!/usr/bin/env bash
exec python3 "$APP_DIR/serial_port_notifier.py"
EOF

chmod +x "$BIN_DIR/serial-port-notifier"

cat > "$AUTOSTART_DIR/serial-port-notifier.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=SerialPortNotifier
Comment=Show a notification when a USB serial port is connected or disconnected
Exec=$BIN_DIR/serial-port-notifier
Terminal=false
X-GNOME-Autostart-enabled=true
EOF

echo
echo "Installation completed."
echo "Executable: $BIN_DIR/serial-port-notifier"
echo "Autostart:   $AUTOSTART_DIR/serial-port-notifier.desktop"
echo
echo "Run now with:"
echo "  $BIN_DIR/serial-port-notifier"
