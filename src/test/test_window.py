import sys
import PyQt5.QtWidgets as QApplication
from src.windows.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication.QApplication(sys.argv)
    windows = MainWindow()
    sys.exit(app.exec_())