from PyQt5.QtWidgets import *

from src.windows.countdown_widget import CountdownWidget
from src.windows.main_canvas import MainCanvas
from src.windows.start_game_dialog import StartGameDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.user_name = None
        self.user_id = None
        
    def initUI(self):
        self.setWindowTitle('你画我猜')
        self.setMinimumSize(800, 600)
        self.setGeometry(100, 100, 800, 600)
        
        
        self.stacked_layout = QStackedLayout()
        self.createMainWidget()
        self.createDrawWidget()
        self.setLayout(self.stacked_layout)
        
        self.show()
        # self.showFullScreen()

    def createMainWidget(self):
        self.main_widget = QWidget()
        
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        
        bt_start_game = QPushButton('start game')
        bt_start_game.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_start_game.setMinimumSize(200, 50)
        bt_start_game.clicked.connect(self.startGame)
        
        bt_setting = QPushButton('setting')
        bt_setting.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_setting.setMinimumSize(200, 50)
        bt_setting.clicked.connect(self.setting)
        
        bt_exit_game = QPushButton('exit game')
        bt_exit_game.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        bt_exit_game.setMinimumSize(200, 50)
        bt_exit_game.clicked.connect(self.exitGame)
        
        left_layout.addStretch(2)
        left_layout.addWidget(bt_start_game,1)
        left_layout.addStretch(1)
        left_layout.addWidget(bt_exit_game,1)
        left_layout.addStretch(2)
        
        main_layout.addLayout(left_layout,1)
        main_layout.addStretch(2)
        self.main_widget.setLayout(main_layout)
        self.stacked_layout.addWidget(self.main_widget)
  
    def createDrawWidget(self):
        self.draw_widget = QWidget()
        
        main_layout = QHBoxLayout()
        
        self.canvas = MainCanvas(self)
        
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        
        self.countdown_widget = CountdownWidget(self)
        
        self.label_words = QLabel('words:')
        self.label_words.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label_words.setMinimumSize(200, 50)
        
        self.label_word_info = QLabel('')
        self.label_word_info.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.label_word_info.setMinimumSize(200, 50)
        
        self.edit_word = QLineEdit(self)
        self.edit_word.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.edit_word.setMinimumSize(200, 50)
        
        self.table_members = QTableWidget(self)
        self.table_members.setColumnCount(2)
        self.table_members.setHorizontalHeaderLabels(['player', 'score'])
        self.table_members.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_members.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        right_layout.addWidget(self.countdown_widget)
        right_layout.addWidget(self.label_words)
        right_layout.addWidget(self.label_word_info)
        right_layout.addWidget(self.edit_word)
        right_layout.addWidget(self.table_members)
        
        right_widget.setLayout(right_layout)
        
        main_layout.addWidget(self.canvas,10)
        main_layout.addWidget(right_widget,1)
        
        self.draw_widget.setLayout(main_layout)
        self.stacked_layout.addWidget(self.draw_widget)
        
    def startGame(self):
        start_game_dialog = StartGameDialog(self)
        start_game_dialog.exec()
        
    def setting(self):
        pass
    
    def exitGame(self):
        self.close()
        
        