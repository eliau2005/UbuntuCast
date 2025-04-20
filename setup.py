#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ubuntucast",
    version="1.0.0",
    author="UbuntuCast Contributors",
    author_email="your.email@example.com",
    description="Screen Casting Tool for Ubuntu Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ubuntucast",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
    install_requires=[
        "PyQt5>=5.15.0",
        "pychromecast>=10.2.3",
        "zeroconf>=0.38.6",
        "python-xlib>=0.31",
        "pulsectl>=22.3.2",
        "ffmpeg-python>=0.2.0",
        "dbus-python>=1.2.18",
        "psutil>=5.9.0",
        "requests>=2.27.1",
        "pillow>=9.0.0",
        "numpy>=1.22.0"
    ],
    entry_points={
        'console_scripts': [
            'ubuntucast=src.ubuntucast:main',
        ],
    },
    include_package_data=True,
    data_files=[
        ('share/applications', ['UbuntuCast.desktop']),
        ('share/ubuntucast', ['config.ini']),
        ('share/icons/hicolor/16x16/apps', ['assets/ubuntucast-16.png']),
        ('share/icons/hicolor/22x22/apps', ['assets/ubuntucast-22.png']),
        ('share/icons/hicolor/24x24/apps', ['assets/ubuntucast-24.png']),
        ('share/icons/hicolor/32x32/apps', ['assets/ubuntucast-32.png']),
        ('share/icons/hicolor/48x48/apps', ['assets/ubuntucast-48.png']),
        ('share/icons/hicolor/64x64/apps', ['assets/ubuntucast-64.png']),
        ('share/icons/hicolor/128x128/apps', ['assets/ubuntucast-128.png']),
        ('share/icons/hicolor/scalable/apps', ['assets/ubuntucast.svg']),
    ],
) 