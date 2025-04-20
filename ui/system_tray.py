#!/usr/bin/env python3
# UbuntuCast - Screen Casting Tool for Ubuntu Linux
# System Tray Icon

import os
import sys
import logging
from PyQt5.QtWidgets import (
    QSystemTrayIcon, QMenu, QAction, QMessageBox, QApplication
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

logger = logging.getLogger("UbuntuCast.UI.SystemTray")

class SystemTrayIcon(QSystemTrayIcon):
    """System tray icon for UbuntuCast"""
    
    def __init__(self, main_window, cast_manager):
        super().__init__()
        
        self.main_window = main_window
        self.cast_manager = cast_manager
        
        # Set icon
        icon_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets/ubuntucast.png"
        )
        if os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
        else:
            # Use fallback icon if custom icon not found
            self.setIcon(QIcon.fromTheme("video-display"))
        
        # Create menu
        self.menu = QMenu()
        self.setup_menu()
        self.setContextMenu(self.menu)
        
        # Connect signals
        self.activated.connect(self.on_activated)
        
        # Register for cast status updates
        self.cast_manager.register_status_callback(self.update_casting_status)
        
        # Set tooltip
        self.setToolTip("UbuntuCast")
    
    def setup_menu(self):
        """Set up the tray icon menu"""
        # Show/hide main window
        self.show_action = QAction("Show UbuntuCast", self)
        self.show_action.triggered.connect(self.main_window.show)
        self.menu.addAction(self.show_action)
        
        # Casting controls
        self.menu.addSeparator()
        
        self.casting_label = QAction("Not casting", self)
        self.casting_label.setEnabled(False)
        self.menu.addAction(self.casting_label)
        
        self.start_action = QAction("Start Casting", self)
        self.start_action.triggered.connect(self.on_start_casting)
        self.menu.addAction(self.start_action)
        
        self.stop_action = QAction("Stop Casting", self)
        self.stop_action.triggered.connect(self.on_stop_casting)
        self.stop_action.setEnabled(False)
        self.menu.addAction(self.stop_action)
        
        # Device selection submenu
        self.device_menu = QMenu("Cast to Device", self.menu)
        self.menu.addMenu(self.device_menu)
        
        # Update device list on show
        self.device_menu.aboutToShow.connect(self.populate_device_menu)
        
        # Exit
        self.menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.on_exit)
        self.menu.addAction(exit_action)
    
    def populate_device_menu(self):
        """Populate the device menu with available cast devices"""
        # Clear existing items
        self.device_menu.clear()
        
        # Get devices from device discovery
        if hasattr(self.cast_manager, '_device_discovery'):
            device_discovery = self.cast_manager._device_discovery
            devices = device_discovery.get_devices()
            
            if devices:
                for uuid, device in devices.items():
                    action = QAction(f"{device['name']} ({device['model_name']})", self)
                    action.setData(uuid)
                    action.triggered.connect(self.on_device_selected)
                    self.device_menu.addAction(action)
            else:
                no_devices = QAction("No devices found", self)
                no_devices.setEnabled(False)
                self.device_menu.addAction(no_devices)
                
                refresh_action = QAction("Refresh devices", self)
                refresh_action.triggered.connect(self.on_refresh_devices)
                self.device_menu.addAction(refresh_action)
        else:
            no_devices = QAction("No devices found", self)
            no_devices.setEnabled(False)
            self.device_menu.addAction(no_devices)
    
    def update_casting_status(self, status):
        """Update UI based on cast status changes"""
        if status == "started":
            self.casting_label.setText("Casting...")
            self.start_action.setEnabled(False)
            self.stop_action.setEnabled(True)
            # Show notification
            self.showMessage(
                "UbuntuCast", 
                f"Casting to {self.cast_manager.current_device.device.friendly_name}",
                QSystemTrayIcon.Information,
                3000
            )
        elif status in ["stopped", "error", "disconnected"]:
            self.casting_label.setText("Not casting")
            self.start_action.setEnabled(True)
            self.stop_action.setEnabled(False)
            # Show notification on disconnect or error
            if status == "disconnected":
                self.showMessage(
                    "UbuntuCast", 
                    "Connection to cast device lost",
                    QSystemTrayIcon.Warning,
                    3000
                )
            elif status == "error":
                self.showMessage(
                    "UbuntuCast",
                    "Error during casting",
                    QSystemTrayIcon.Critical,
                    3000
                )
    
    @pyqtSlot(QSystemTrayIcon.ActivationReason)
    def on_activated(self, reason):
        """Handle tray icon activation"""
        if reason == QSystemTrayIcon.Trigger:
            # Toggle main window visibility
            if self.main_window.isVisible():
                self.main_window.hide()
            else:
                self.main_window.show()
    
    @pyqtSlot()
    def on_start_casting(self):
        """Handle start casting menu action"""
        # Check if a device is selected
        if not self.cast_manager.current_device:
            self.showMessage(
                "UbuntuCast",
                "No device selected. Please select a device first.",
                QSystemTrayIcon.Warning,
                3000
            )
            return
        
        # Set default options for casting
        self.cast_manager.set_cast_mode("screen")
        self.cast_manager.set_audio_enabled(True)
        
        # Start casting
        success = self.cast_manager.start_casting()
        
        if not success:
            self.showMessage(
                "UbuntuCast",
                "Failed to start casting. Check logs for details.",
                QSystemTrayIcon.Critical,
                3000
            )
    
    @pyqtSlot()
    def on_stop_casting(self):
        """Handle stop casting menu action"""
        self.cast_manager.stop_casting()
    
    @pyqtSlot()
    def on_device_selected(self):
        """Handle device selection from menu"""
        action = self.sender()
        if action:
            device_uuid = action.data()
            if device_uuid:
                success = self.cast_manager.select_device(device_uuid)
                if success:
                    self.showMessage(
                        "UbuntuCast",
                        f"Selected device: {self.cast_manager.current_device.device.friendly_name}",
                        QSystemTrayIcon.Information,
                        3000
                    )
                else:
                    self.showMessage(
                        "UbuntuCast",
                        "Failed to connect to selected device",
                        QSystemTrayIcon.Warning,
                        3000
                    )
    
    @pyqtSlot()
    def on_refresh_devices(self):
        """Handle refresh devices menu action"""
        if hasattr(self.cast_manager, '_device_discovery'):
            device_discovery = self.cast_manager._device_discovery
            device_discovery.stop_discovery()
            device_discovery.start_discovery()
            
            self.showMessage(
                "UbuntuCast",
                "Refreshing cast devices...",
                QSystemTrayIcon.Information,
                2000
            )
    
    @pyqtSlot()
    def on_exit(self):
        """Handle exit menu action"""
        # Check if we're casting
        if self.cast_manager.is_casting:
            reply = QMessageBox.question(
                None,
                "UbuntuCast",
                "You are currently casting. Are you sure you want to exit?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.No:
                return
            
            # Stop casting if it's active
            self.cast_manager.stop_casting()
        
        # Stop device discovery
        if hasattr(self.cast_manager, '_device_discovery'):
            device_discovery = self.cast_manager._device_discovery
            device_discovery.stop_discovery()
        
        # Save config
        config_path = os.path.expanduser("~/.config/ubuntucast/config.ini")
        with open(config_path, 'w') as config_file:
            self.cast_manager.config.write(config_file)
        
        # Quit application
        QApplication.quit() 