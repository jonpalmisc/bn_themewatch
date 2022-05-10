# Copyright (c) 2022 Jon Palmisciano. All rights reserved.
#
# Use of this source code is governed by the BSD 3-Clause license; the full
# terms of the license can be found in the LICENSE.txt file.

from binaryninja import execute_on_main_thread, log_info, user_directory
from binaryninjaui import resetUserThemes

from PySide6.QtCore import QFileSystemWatcher

from os import path

# Create globally to prevent garbage collection
watcher = QFileSystemWatcher()


def reloadTheme():
    log_info("Reloading user themes")
    resetUserThemes()


def handleChange(_):
    execute_on_main_thread(reloadTheme)


def start():
    themeDir = path.join(user_directory(), "themes")

    watcher.addPath(themeDir)
    watcher.directoryChanged.connect(handleChange)

    log_info("Watching for changes to user themes")
