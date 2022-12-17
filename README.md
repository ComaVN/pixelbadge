# Curious Supplies Pixel Badge Sandbox

The udev rule I use to make a `/dev/pixelbadge` alias (works on Ubuntu 22.04.1 LTS "yammy"):
```
$ cat /etc/udev/rules.d/99-local-rh.pixel-badge.rules
# Curious Supplies Pixel Badge
# The Pixel Badge is a devboard with 256 beautiful full-colour LEDs, a WiFi-enabled ESP32 WROOM microcontroller, tactile switches, and USB-C connectivity. It runs MicroPython apps, and can be powered via USB or an 18650 lithium-ion battery.
# https://pixel.curious.supplies/
KERNEL=="ttyUSB[0-9]", SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", MODE="0666", SYMLINK+="pixelbadge"
```

To connect:
```
screen /dev/pixelbadge 115200
```

To disconnect, press `Ctrl`-`A` followed by `k`
