# UbuntuCast

A screen casting tool for Ubuntu Linux that allows casting your screen to Chromecast devices and other Google Cast-compatible receivers.

## Features

- Cast your entire screen or a specific window
- Stream audio along with video
- Discover and connect to Cast devices on your network
- Support for various resolutions and framerates
- Minimal UI with system tray integration
- Integration with Ubuntu desktop environments (GNOME, Unity, KDE, XFCE)
- Support for both X11 and Wayland sessions

## Installation

### From source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ubuntucast.git
cd ubuntucast
```

2. Install dependencies:
```bash
sudo apt install python3-pip ffmpeg libpulse-dev python3-pyqt5 xdotool wmctrl
pip3 install -r requirements.txt
```

3. Install the package:
```bash
pip3 install .
```

### Optional dependencies

For Wayland support:
```bash
sudo apt install wf-recorder
```

## Usage

Launch UbuntuCast from your application menu or run:

```bash
ubuntucast
```

1. Select a casting device from the list
2. Choose whether to cast your entire screen or a specific window
3. Configure audio settings if needed
4. Click "Start Casting"

## Requirements

- Ubuntu 20.04 or newer
- Python 3.8+
- FFmpeg
- PulseAudio
- A Chromecast or other Google Cast compatible device

## Troubleshooting

- If you're using Wayland and experiencing issues, try installing wf-recorder for better screen capture support
- If no devices are found, ensure your Chromecast and computer are on the same network
- For audio issues, check your PulseAudio configuration

## License

MIT License 