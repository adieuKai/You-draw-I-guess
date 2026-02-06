from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QPushButton,QSizePolicy,QHBoxLayout

from PyQt5.QtWidgets import QDialog

class base_dialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.baseInitUI()
        
    def baseInitUI(self):
        self.setWindowFlags(Qt.Dialog | 
                            Qt.WindowTitleHint | 
                            Qt.WindowCloseButtonHint)
        
        self.basereatToolButton()
        
    def basereatToolButton(self):
        self.widget_tool = QWidget()
        main_layout = QHBoxLayout()
        
        self.bt_ok = QPushButton('OK')
        self.bt_ok.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.bt_ok.setMinimumSize(200, 50)
        
        self.bt_cancel = QPushButton('Cancel')
        self.bt_cancel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.bt_cancel.setMinimumSize(200, 50)
    
        main_layout.addStretch(1)
        main_layout.addWidget(self.bt_ok)
        main_layout.addStretch(1)
        main_layout.addWidget(self.bt_cancel)
        main_layout.addStretch(1)
        
        self.widget_tool.setLayout(main_layout)
        self.widget_tool.hide()
      