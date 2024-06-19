from PyQt6.QtWidgets import QApplication
import sys
from app.main_window import MainWindow


def start():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()


if __name__ == '__main__':
    start()