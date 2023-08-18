from PyQt5.QtWidgets import QApplication

import console
import window
import sys


file_path = "task_presets.json"
# console = console.Console(file_path)
# console.start()
app = QApplication(sys.argv)
window = window.Window(file_path)
sys.exit(app.exec_())
