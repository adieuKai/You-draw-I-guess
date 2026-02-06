from PyQt5.QtWidgets import (QStackedLayout,QWidget,QPushButton,QLayout,
                             QLabel,QVBoxLayout,QHBoxLayout,QSizePolicy,
                             QTableWidget,QHeaderView,QGridLayout,QLineEdit,
                             QComboBox)

from src.windows.add_room_dialog import AddRoomDialog
from src.windows.base_dialog import base_dialog


class StartGameDialog(base_dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle('create')
        self.setMinimumSize(660, 440)
                
        self.stacked_layout = QStackedLayout()
        
        self.createRoomListWidget()
        self.createMainRoomWidget()

        self.setLayout(self.stacked_layout)
        
    def createRoomListWidget(self):
        self.page_room_table = QWidget()
        main_layout = QHBoxLayout()
        
        # 房间列表
        self.room_table = QTableWidget()
        self.room_table.setColumnCount(4)
        self.room_table.setHorizontalHeaderLabels(['Room Name','Homeowner','Clocked', 'Players', 'Status'])
        self.room_table.setColumnWidth(0, 250)
        self.room_table.setColumnWidth(1, 100)
        self.room_table.setColumnWidth(2, 80)
        self.room_table.setColumnWidth(3, 80)
        self.room_table.setColumnWidth(4, 80)
        self.room_table.setRowCount(12)
        horizontal_header = self.room_table.horizontalHeader()
        horizontal_header.setSectionResizeMode(0, QHeaderView.Stretch)
        horizontal_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        horizontal_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        horizontal_header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.room_table.verticalHeader().setVisible(False)
        self.room_table.verticalHeader().setMinimumSectionSize(30)
        self.room_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 右侧按钮
        right_layout = QVBoxLayout()
        bt_create_room = QPushButton('create room')
        bt_create_room.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_create_room.setMinimumSize(200, 50)
        bt_create_room.clicked.connect(self.createRoom)
        
        bt_add_room = QPushButton('add room')
        bt_add_room.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_add_room.setMinimumSize(200, 50)
        bt_add_room.clicked.connect(self.addRoom)
        
        bt_quick_add = QPushButton('quick add')
        bt_quick_add.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_quick_add.setMinimumSize(200, 50)
        # bt_quick_add.clicked.connect(self.quickAddRoom)
        
        bt_back = QPushButton('back')
        bt_back.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_back.setMinimumSize(200, 50)
        # bt_back.clicked.connect(self.back)
        
        right_layout.addWidget(bt_create_room,1)
        right_layout.addStretch(1)
        right_layout.addWidget(bt_add_room,1)
        right_layout.addStretch(1)
        right_layout.addWidget(bt_quick_add,1)
        right_layout.addStretch(10)
        right_layout.addWidget(bt_back,1)
        
        main_layout.addWidget(self.room_table,10)
        main_layout.addLayout(right_layout,1)
        
        self.page_room_table.setLayout(main_layout)
        self.stacked_layout.addWidget(self.page_room_table)

    def createMainRoomWidget(self):
        self.page_main_room = QWidget()
        main_layout = QVBoxLayout()
        
        top_widget = QWidget()
        top_layout = QHBoxLayout()
        self.label_title = QLabel('room name')
        self.label_title.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label_title.setMinimumSize(200, 50)
        
        self.bt_room_setting = QPushButton('setting')
        self.bt_room_setting.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.bt_room_setting.setMinimumSize(200, 50)
        
        self.bt_begin = QPushButton('begin')
        self.bt_begin.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.bt_begin.setMinimumSize(200, 50)
        
        
        top_layout.addWidget(self.label_title,1)
        top_layout.addStretch(10)
        top_layout.addWidget(self.bt_room_setting,1)
        top_layout.addWidget(self.bt_begin,1)
        top_widget.setLayout(top_layout)
        
        self.table_member = QTableWidget()
        self.table_member.setColumnCount(1)
        self.table_member.setHorizontalHeaderLabels(['Player'])
        self.table_member.setRowCount(0)
        self.table_member.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
              
        main_layout.addWidget(top_widget,1)
        main_layout.addWidget(self.table_member,10)
        
        self.page_main_room.setLayout(main_layout)
        self.stacked_layout.addWidget(self.page_main_room)

    def createRoom(self):
        add_room_dialog = AddRoomDialog(self)
        add_room_dialog.exec_()
        if add_room_dialog.accepted:
            pass
    
    def addRoom(self):
        self.stacked_layout.setCurrentWidget(self.page_main_room)

