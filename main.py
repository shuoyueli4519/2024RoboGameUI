import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QLinearGradient, QPainter, QPixmap, QColor, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QPushButton, QFileDialog, QStackedLayout

class MainWindow(QMainWindow):
    def InitUI(self):
        self.setWindowTitle("2024RoboGameUI")
        screen = QDesktopWidget().screenGeometry()
        self.screen_width, self.screen_height = screen.width(), screen.height()
        self.resize(self.screen_width, self.screen_height)
        
        self.background = QLabel(self)
        pixmap_background = QPixmap("assets/background.png")
        self.background.setPixmap(pixmap_background)
        self.background.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.background.setScaledContents(True)
        
        self.main_timer = QTimer(self)
        self.main_timer.timeout.connect(self.update)
        self.main_time_left = 420
        self.fangdai = 420
        self.fangdai_lock = 0
        self.red_team_flag = 0
        self.blue_team_flag = 0
        
        self.main_timer_label = QLabel(self)
        self.main_timer_label.setText("07:00")
        self.main_timer_label.setStyleSheet("QLabel{font-size:" + str(int(self.screen_width/1920 * 150 + self.screen_height/1080 * 150)) + "px; \
                                                    font-weight:bold; \
                                                    font-family:Microsoft YaHei; \
                                                    color: white;}")
        self.main_timer_label.setAlignment(Qt.AlignCenter)
        self.main_timer_label.setGeometry(int(self.screen_width * 0.15), int(self.screen_height * 0.25),
                                          int(self.screen_width * 0.7), int(self.screen_height * 0.4))
        
        self.start_game = QPushButton(self)
        self.start_game.setGeometry(int(self.screen_width * 0.3), int(self.screen_height * 0.65),
                                      int(self.screen_width * 0.16), int(self.screen_height * 0.08))
        icon = QIcon("assets/start.png")
        self.start_game.setIcon(icon)
        self.start_game.setIconSize(self.start_game.size())
        self.start_game.setStyleSheet("QPushButton{border: 0px solid white; \
                                        border-radius: 10px;}")
        self.start_game.clicked.connect(self.start_game_clicked)
        
        self.reset = QPushButton(self)
        self.reset.setGeometry(int(self.screen_width * 0.42), int(self.screen_height * 0.65),
                                int(self.screen_width * 0.16), int(self.screen_height * 0.08))
        pixmap = QPixmap("assets/reset.png")
        icon = QIcon(pixmap)
        self.reset.setIcon(icon)
        self.reset.setIconSize(self.reset.size())
        self.reset.setStyleSheet("QPushButton{border: 0px solid white; \
                                        border-radius: 10px;}")
        self.reset.clicked.connect(self.reset_clicked)
        
        self.game_status = QLabel(self)
        self.game_status.setGeometry(int(self.screen_width * 0.3), int(self.screen_height * 0.18),
                                    int(self.screen_width * 0.3), int(self.screen_height * 0.18))
        pixmap = QPixmap("assets/waitgame.png")
        self.game_status.setPixmap(pixmap)
        self.game_status.setScaledContents(True)
        
        self.red_team = QPushButton(self)
        self.red_team.setGeometry(int(self.screen_width * 0.45), int(self.screen_height * 0),
                                    int(self.screen_width * 0.5), int(self.screen_height * 0.3))
        pixmap = QPixmap("assets/redteam.png")
        icon = QIcon(pixmap)
        self.red_team.setIcon(icon)
        self.red_team.setIconSize(self.red_team.size())
        self.red_team.setStyleSheet("QPushButton{border: 0px solid white; \
                                        border-radius: 10px;}")
        self.red_team.clicked.connect(self.red_team_clicked)
        
        self.red_team_status = QLabel(self)
        pixmap = QPixmap("assets/redwaitstatus.png")
        self.red_team_status.setPixmap(pixmap)
        self.red_team_status.setScaledContents(True)
        self.red_team_status.setGeometry(int(self.screen_width * 0.8), int(self.screen_height * 0.1),
                                        int(self.screen_width * 0.18), int(self.screen_height * 0.6))
        
        self.blue_team = QPushButton(self)
        self.blue_team.setGeometry(int(self.screen_width * 0.05), int(self.screen_height * 0.6),
                                    int(self.screen_width * 0.5), int(self.screen_height * 0.4))
        pixmap = QPixmap("assets/blueteam.png")
        icon = QIcon(pixmap)
        self.blue_team.setIcon(icon)
        self.blue_team.setIconSize(self.blue_team.size())
        self.blue_team.setStyleSheet("QPushButton{border: 0px solid white; \
                                        border-radius: 10px;}")
        
        self.blue_team_status = QLabel(self)
        pixmap = QPixmap("assets/bluewaitstatus.png")
        self.blue_team_status.setPixmap(pixmap)
        self.blue_team_status.setScaledContents(True)
        self.blue_team_status.setGeometry(int(self.screen_width * 0.02), int(self.screen_height * 0.3),
                                        int(self.screen_width * 0.18), int(self.screen_height * 0.6))
        self.blue_team.clicked.connect(self.blue_team_clicked)
        
        self.reset.raise_()
        self.start_game.raise_()
        
    def blue_team_clicked(self):
        self.blue_team_flag = 1 - self.blue_team_flag
        if self.blue_team_flag == 1:
            pixmap = QPixmap("assets/bluewrong.png")
            self.blue_team_status.setPixmap(pixmap)
        else:
            pixmap = QPixmap("assets/bluegaming.png")
            self.blue_team_status.setPixmap(pixmap)
        
    def red_team_clicked(self):
        self.red_team_flag = 1 - self.red_team_flag
        if self.red_team_flag == 1:
            pixmap = QPixmap("assets/redwrong.png")
            self.red_team_status.setPixmap(pixmap)
        else:
            pixmap = QPixmap("assets/redgaming.png")
            self.red_team_status.setPixmap(pixmap)
        
    def start_game_clicked(self):
        self.fangdai_lock = 1
        pixmap = QPixmap("assets/gaming.png")
        self.game_status.setPixmap(pixmap)
        self.main_timer.start(1000)
        pixmap = QPixmap("assets/redgaming.png")
        self.red_team_status.setPixmap(pixmap)
        pixmap_blue = QPixmap("assets/bluegaming.png")
        self.blue_team_status.setPixmap(pixmap_blue)
        
    def reset_clicked(self):
        if self.main_time_left < 420:
            self.fangdai = self.main_time_left
        self.fangdai_lock = 0
        self.main_timer.stop()
        self.main_time_left = 420
        self.main_timer_label.setText("07:00")
        pixmap = QPixmap("assets/waitgame.png")
        self.game_status.setPixmap(pixmap)
        pixmap = QPixmap("assets/redwaitstatus.png")
        self.red_team_status.setPixmap(pixmap)
        pixmap_blue = QPixmap("assets/bluewaitstatus.png")
        self.blue_team_status.setPixmap(pixmap_blue)
        
    def update(self):
        self.main_time_left -= 1
        if self.main_time_left >= 0:
            minutes = self.main_time_left // 60
            seconds = self.main_time_left % 60
            self.main_timer_label.setText("{:02d}:{:02d}".format(minutes, seconds))
        else:
            self.main_timer.stop()
            self.main_timer_label.setText("00:00")
            pixmap = QPixmap("assets/redwaitstatus.png")
            self.red_team_status.setPixmap(pixmap)
            pixmap_blue = QPixmap("assets/bluewaitstatus.png")
            self.blue_team_status.setPixmap(pixmap_blue)
            pixmap = QPixmap("assets/endgame.png")
            self.game_status.setPixmap(pixmap)
        
    def __init__(self):
        super().__init__()
        self.InitUI()
        
    def keyPressEvent(self, envent):
        key = envent.key()
        modif = envent.modifiers()
        if key == Qt.Key_Escape or key == Qt.Key_Q:
            self.close()
        if modif == Qt.ControlModifier and key == Qt.Key_Return:
            self.start_game_clicked()
        if modif == Qt.ControlModifier and key == Qt.Key_C:
            self.reset_clicked()
        if modif == Qt.ControlModifier and key == Qt.Key_R and self.fangdai_lock == 0:
            self.start_game_clicked()
            self.fangdai_lock = 1
            self.main_time_left = self.fangdai
        if key == Qt.Key_L and self.fangdai_lock == 1:
            self.red_team_clicked()
        if key == Qt.Key_A and self.fangdai_lock == 1:
            self.blue_team_clicked()
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showFullScreen()
    mainWindow.show()
    sys.exit(app.exec_())
    