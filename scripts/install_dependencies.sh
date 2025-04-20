#!/bin/bash
# UbuntuCast dependencies installation script
# This script installs all required dependencies for UbuntuCast on Ubuntu

# Exit on error
set -e

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

echo "Installing UbuntuCast dependencies..."

# Update package lists
apt update

# Install system dependencies
apt install -y python3 python3-pip python3-pyqt5 python3-dbus ffmpeg libpulse-dev xdotool wmctrl

# Install Wayland support
apt install -y wf-recorder

# Install Python dependencies
pip3 install PyQt5>=5.15.0 pychromecast>=10.2.3 zeroconf>=0.38.6 python-xlib>=0.31 pulsectl>=22.3.2 \
  ffmpeg-python>=0.2.0 dbus-python>=1.2.18 psutil>=5.9.0 requests>=2.27.1 pillow>=9.0.0 numpy>=1.22.0

# Set up desktop integration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Create desktop file if it doesn't exist
if [ -f "$PROJECT_DIR/UbuntuCast.desktop" ]; then
  echo "Installing desktop file..."
  cp "$PROJECT_DIR/UbuntuCast.desktop" /usr/share/applications/
  
  # Create symlink to executable
  if [ -f "$PROJECT_DIR/ubuntucast.py" ]; then
    echo "Creating executable symlink..."
    ln -sf "$PROJECT_DIR/ubuntucast.py" /usr/local/bin/ubuntucast
    chmod +x "$PROJECT_DIR/ubuntucast.py"
  fi
fi

echo "UbuntuCast dependencies installation complete!"
echo "You can now run UbuntuCast from your application menu or by typing 'ubuntucast' in the terminal." 