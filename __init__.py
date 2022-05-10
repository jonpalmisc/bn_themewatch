# Copyright (c) 2022 Jon Palmisciano. All rights reserved.
#
# Use of this source code is governed by the BSD 3-Clause license; the full
# terms of the license can be found in the LICENSE.txt file.

from binaryninja import core_ui_enabled, log_info

if core_ui_enabled():
    from . import themewatch

    log_info("UI is enabled, loading ThemeWatch")
    themewatch.start()
