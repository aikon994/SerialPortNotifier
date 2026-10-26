#!/usr/bin/env python3
import time
import threading
import subprocess
import shutil
import tkinter as tk
from serial.tools import list_ports

POLL_INTERVAL = 0.8

def get_ports():
    ports = {}
    for p in list_ports.comports():
        ports[p.device] = {
            "device": p.device,
            "description": p.description or "Serial device",
            "manufacturer": p.manufacturer or "",
            "vid": f"{p.vid:04X}" if p.vid is not None else "",
            "pid": f"{p.pid:04X}" if p.pid is not None else "",
            "serial_number": p.serial_number or "",
        }
    return ports

def notify_native(title, body):
    if shutil.which("notify-send"):
        subprocess.run(["notify-send", title, body], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        return True
    return False

class Popup:
    def __init__(self, root):
        self.root = root
        self.windows = []

    def show(self, title, info, connected=True):
        lines = [f"Port: {info['device']}", info["description"]]
        if info.get("manufacturer"):
            lines.append(f"Manufacturer: {info['manufacturer']}")
        if info.get("vid") and info.get("pid"):
            lines.append(f"VID:PID {info['vid']}:{info['pid']}")
        if info.get("serial_number"):
            lines.append(f"Serial: {info['serial_number']}")
        body = "\n".join(lines)
        if notify_native(title, body):
            return
        w = tk.Toplevel(self.root)
        w.overrideredirect(True)
        w.attributes("-topmost", True)
        width, height = 420, 190
        sw = w.winfo_screenwidth()
        sh = w.winfo_screenheight()
        offset = len(self.windows) * (height + 10)
        x = sw - width - 20
        y = sh - height - 70 - offset
        w.geometry(f"{width}x{height}+{x}+{y}")
        outer = tk.Frame(w, bg="#1f1f1f", highlightthickness=1, highlightbackground="#555")
        outer.pack(fill="both", expand=True)
        top = tk.Frame(outer, bg="#2b2b2b")
        top.pack(fill="x")
        icon = "●" if connected else "○"
        tk.Label(top, text=f"{icon}  {title}", fg="white", bg="#2b2b2b", font=("Sans", 12, "bold"), anchor="w", padx=12, pady=10).pack(side="left", fill="x", expand=True)
        close = tk.Label(top, text="✕", fg="#dddddd", bg="#2b2b2b", font=("Sans", 11), padx=12, cursor="hand2")
        close.pack(side="right")
        close.bind("<Button-1>", lambda e: self.close(w))
        tk.Label(outer, text=body, justify="left", fg="#f4f4f4", bg="#1f1f1f", font=("Sans", 10), anchor="nw", padx=14, pady=12).pack(fill="both", expand=True)
        self.windows.append(w)
        w.after(6500, lambda: self.close(w))

    def close(self, w):
        try:
            if w in self.windows:
                self.windows.remove(w)
            w.destroy()
        except Exception:
            pass

def monitor(root, popup):
    previous = get_ports()
    root.after(300, lambda: popup.show("Serial Port Notifier started", {
        "device": "Monitor active",
        "description": "Waiting for a serial port change",
        "manufacturer": "",
        "vid": "",
        "pid": "",
        "serial_number": ""
    }, True))
    while True:
        time.sleep(POLL_INTERVAL)
        current = get_ports()
        added = set(current) - set(previous)
        removed = set(previous) - set(current)
        for dev in sorted(added):
            info = current[dev]
            root.after(0, lambda i=info: popup.show("USB serial connected", i, True))
        for dev in sorted(removed):
            info = previous[dev]
            root.after(0, lambda i=info: popup.show("USB serial disconnected", i, False))
        previous = current

def main():
    root = tk.Tk()
    root.withdraw()
    popup = Popup(root)
    threading.Thread(target=monitor, args=(root, popup), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()
