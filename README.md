# UbuntuCast

Here's how to install UbuntuCast on Ubuntu:

## Prerequisites

First, install the required system dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-pyqt5 python3-dbus ffmpeg libpulse-dev xdotool wmctrl
```

For Wayland support (optional but recommended if you use Wayland):
```bash
sudo apt install -y wf-recorder
```

## Installation

### Method 1: Direct Installation from Source

1. Navigate to the UbuntuCast directory:
```bash
cd UbuntuCast
```

2. Install using pip:
```bash
pip3 install .
```

3. If you prefer to install for your user only (no sudo required):
```bash
pip3 install --user .
```

### Method 2: Using the Installation Script

If a scripts/install_dependencies.sh file is included:

```bash
cd UbuntuCast
sudo ./scripts/install_dependencies.sh
```

## Post-Installation Setup

After installation, ensure the desktop file is properly installed:

```bash
# Copy desktop file for system-wide integration
sudo cp UbuntuCast.desktop /usr/share/applications/

# Create the log directory if needed
mkdir -p ~/.local/share/ubuntucast/logs
```

## Running UbuntuCast

You can now run UbuntuCast from your application launcher or by typing:

```bash
ubuntucast
```

## Troubleshooting

If you encounter any issues:

- Make sure all dependencies are installed
- Check log files in `~/.local/share/ubuntucast/logs/`
- Verify the application has proper permissions
