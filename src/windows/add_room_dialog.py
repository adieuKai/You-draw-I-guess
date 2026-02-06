from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QLineEdit, QComboBox, QSizePolicy

from src.windows.base_dialog import base_dialog

class AddRoomDialog(base_dialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Add Room')
        self.setMinimumSize(400, 300)
        
        main_layout = QVBoxLayout()
        
        grid_layout = QGridLayout()
        
        label_room_name = QLabel('Room Name:')
        label_room_name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        label_room_name.setMinimumSize(100, 50)
        grid_layout.addWidget(label_room_name,0,0)
        
        self.edit_room_name = QLineEdit()
        self.edit_room_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grid_layout.addWidget(self.edit_room_name,0,1)
        
        label_room_pwd = QLabel('Room Password:')
        label_room_pwd.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        label_room_pwd.setMinimumSize(100, 50)
        grid_layout.addWidget(label_room_pwd,1,0)
        
        self.edit_room_pwd = QLineEdit()
        self.edit_room_pwd.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        grid_layout.addWidget(self.edit_room_pwd,1,1)
        
        label_room_numer = QLabel('Room Number:')
        label_room_numer.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        label_room_numer.setMinimumSize(100, 50)
        grid_layout.addWidget(label_room_numer,2,0)
        
        self.combo_room_num = QComboBox()
        self.combo_room_num.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.combo_room_num.addItem('2',2)
        self.combo_room_num.addItem('4',4)
        self.combo_room_num.addItem('6',6)
        grid_layout.addWidget(self.combo_room_num,2,1)
        
        main_layout.addLayout(grid_layout,10)
        main_layout.addWidget(self.widget_tool,1)
        self.widget_tool.show()
        
        self.setLayout(main_layout)
        
        
        
