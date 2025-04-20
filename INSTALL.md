# UbuntuCast Installation Guide

This document provides instructions for installing UbuntuCast on Ubuntu Linux.

## Dependencies

UbuntuCast requires the following dependencies:

- Python 3.8 or higher
- PyQt5
- pychromecast
- zeroconf
- python-xlib
- pulsectl
- ffmpeg
- dbus-python
- psutil
- requests
- pillow
- numpy
- xdotool
- wmctrl
- ffmpeg
- libpulse-dev

For Wayland support:
- wf-recorder

## Installation Methods

### Method 1: Using the Installation Script

The easiest way to install UbuntuCast and all its dependencies is to use the provided installation script:

```bash
cd UbuntuCast/scripts
sudo ./install_dependencies.sh
```

### Method 2: Manual Installation

1. Install system dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-pyqt5 python3-dbus ffmpeg libpulse-dev xdotool wmctrl
```

2. For Wayland support:

```bash
sudo apt install -y wf-recorder
```

3. Install Python dependencies:

```bash
pip3 install -r requirements.txt
```

4. Install UbuntuCast:

```bash
sudo python3 setup.py install
```

## Desktop Integration

To integrate UbuntuCast with your desktop environment:

```bash
cp UbuntuCast.desktop ~/.local/share/applications/
```

To enable autostart:

```bash
mkdir -p ~/.config/autostart
cp UbuntuCast.desktop ~/.config/autostart/
```

## Running UbuntuCast

After installation, you can run UbuntuCast from your application menu or by typing:

```bash
ubuntucast
```

## Troubleshooting

If you encounter any issues, please refer to the troubleshooting section in the README.md file. 