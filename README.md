# Curious Supplies Pixel Badge Sandbox

## Serial console

The udev rule I use to make a `/dev/pixelbadge` alias:
```
$ cat /etc/udev/rules.d/99-local-rh.pixel-badge.rules
# Curious Supplies Pixel Badge
# The Pixel Badge is a devboard with 256 beautiful full-colour LEDs, a WiFi-enabled ESP32 WROOM microcontroller, tactile switches, and USB-C connectivity. It runs MicroPython apps, and can be powered via USB or an 18650 lithium-ion battery.
# https://pixel.curious.supplies/
KERNEL=="ttyUSB[0-9]", SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", MODE="0666", SYMLINK+="pixelbadge"
```

(verified to work on Ubuntu 22.04.1 LTS "yammy", 23.10 "Mantic Minotaur" and 24.04.1 LTS "Noble Numbat")

To connect:
```
screen /dev/pixelbadge 115200
```

To disconnect, press `Ctrl`-`A` followed by `k`

## Web GUI

The [web GUI](https://webserial.curious.supplies/#/) allows you to install apps, update the device, and set appconfig values. It needs a browser that supports WebSerial, like Chrome.

If you're running eg. Chromium using snap, you might need to allow access to USB to see any TTYs:
```
sudo snap connect chromium:raw-usb
```
