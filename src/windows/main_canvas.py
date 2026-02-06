from PyQt5.QtWidgets import QGraphicsView

class MainCanvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)