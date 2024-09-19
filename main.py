import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QLinearGradient, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QPushButton, QFileDialog

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
        self.red_team_flag = 0
        self.blue_team_flag = 0
        
        self.main_timer_label = QLabel(self)
        self.main_timer_label.setText("07:00")
        self.main_timer_label.setStyleSheet("QLabel{font-size:" + str(int(self.screen_width/1920 * 150 + self.screen_height/1080 * 150)) + "px; \
                                                    font-weight:bold; \
                                                    font-family:Microsoft YaHei; \
                                                    color: white;}")
        self.main_timer_label.setAlignment(Qt.AlignCenter)
        self.main_timer_label.setGeometry(int(self.screen_width * 0.15), int(self.screen_height * 0.2),
                                          int(self.screen_width * 0.7), int(self.screen_height * 0.4))
        
        self.start_game = QPushButton(self)
        self.start_game.setText("开始比赛")
        self.start_game.setStyleSheet(" QPushButton{font-size:" + str(int(self.screen_width/1920 * 10 + self.screen_height/1080 * 10)) + "px; \
                                        font-weight:bold; \
                                        font-family:Microsoft YaHei; \
                                        color: white; \
                                        border: 2px solid white; \
                                        border-radius: 10px;}")
        self.start_game.setGeometry(int(self.screen_width * 0.38), int(self.screen_height * 0.7),
                                      int(self.screen_width * 0.1), int(self.screen_height * 0.05))
        self.start_game.clicked.connect(self.start_game_clicked)
        
        self.reset = QPushButton(self)
        self.reset.setText("复位")
        self.reset.setStyleSheet("  QPushButton{font-size:" + str(int(self.screen_width/1920 * 10 + self.screen_height/1080 * 10)) + "px; \
                                    font-weight:bold; \
                                    font-family:Microsoft YaHei; \
                                    color: white; \
                                    border: 2px solid white; \
                                    border-radius: 10px;}")
        self.reset.setGeometry(int(self.screen_width * 0.52), int(self.screen_height * 0.7),
                                int(self.screen_width * 0.1), int(self.screen_height * 0.05))
        self.reset.clicked.connect(self.reset_clicked)
        
        self.game_status = QLabel(self)
        self.game_status.setText("等待比赛中...")
        self.game_status.setStyleSheet("QLabel{font-size:" + str(int(self.screen_width/1920 * 40 + self.screen_height/1080 * 40)) + "px; \
                                        font-weight:bold; \
                                        font-family:Microsoft YaHei; \
                                        color: white;}")
        self.game_status.setAlignment(Qt.AlignCenter)
        self.game_status.setGeometry(int(self.screen_width * 0.35), int(self.screen_height * 0.15),
                                    int(self.screen_width * 0.3), int(self.screen_height * 0.1))
        
        self.red_team = QPushButton(self)
        self.red_team.setText("红方")
        self.red_team.setStyleSheet("   QPushButton{font-size:" + str(int(self.screen_width/1920 * 40 + self.screen_height/1080 * 40)) + "px; \
                                        font-weight:bold; \
                                        font-family:Microsoft YaHei; \
                                        border-radius: 10px; \
                                        color: red;}")
        self.red_team.setGeometry(int(self.screen_width * 0.08), int(self.screen_height * 0.2),
                                    int(self.screen_width * 0.15), int(self.screen_height * 0.1))
        self.red_team.clicked.connect(self.red_team_clicked)
        
        self.red_team_status = QLabel(self)
        self.red_team_status.setText("等<br>待<br>中")
        self.red_team_status.setStyleSheet("QLabel{font-size:" + str(int(self.screen_width/1920 * 40 + self.screen_height/1080 * 40)) + "px; \
                                            font-weight:bold; \
                                            font-family:Microsoft YaHei; \
                                            color: white; }")
        self.red_team_status.setGeometry(int(self.screen_width * 0.13), int(self.screen_height * 0.3),
                                        int(self.screen_width * 0.15), int(self.screen_height * 0.5))
        
        self.blue_team = QPushButton(self)
        self.blue_team.setText("蓝方")
        self.blue_team.setStyleSheet("  QPushButton{font-size:" + str(int(self.screen_width/1920 * 40 + self.screen_height/1080 * 40)) + "px; \
                                        font-weight:bold; \
                                        font-family:Microsoft YaHei; \
                                        border-radius: 10px; \
                                        color: blue;}")
        self.blue_team.setGeometry(int(self.screen_width * 0.77), int(self.screen_height * 0.2),
                                    int(self.screen_width * 0.15), int(self.screen_height * 0.1))
        
        self.blue_team_status = QLabel(self)
        self.blue_team_status.setText("等<br>待<br>中")
        self.blue_team_status.setStyleSheet("QLabel{font-size:" + str(int(self.screen_width/1920 * 40 + self.screen_height/1080 * 40)) + "px; \
                                            font-weight:bold; \
                                            font-family:Microsoft YaHei; \
                                            color: white; }")
        self.blue_team_status.setGeometry(int(self.screen_width * 0.82), int(self.screen_height * 0.3),
                                        int(self.screen_width * 0.15), int(self.screen_height * 0.5))
        self.blue_team.clicked.connect(self.blue_team_clicked)
        
    def blue_team_clicked(self):
        self.blue_team_flag = 1 - self.blue_team_flag
        if self.blue_team_flag == 1:
            self.blue_team_status.setText("异<br>常<br>处<br>理<br>中")
        else:
            self.blue_team_status.setText("顺<br>利<br>进<br>行<br>中")
        
    def red_team_clicked(self):
        self.red_team_flag = 1 - self.red_team_flag
        if self.red_team_flag == 1:
            self.red_team_status.setText("异<br>常<br>处<br>理<br>中")
        else:
            self.red_team_status.setText("顺<br>利<br>进<br>行<br>中")
        
    def start_game_clicked(self):
        self.game_status.setText("比赛进行中...")
        self.main_timer.start(1000)
        self.red_team_status.setText("顺<br>利<br>进<br>行<br>中")
        self.blue_team_status.setText("顺<br>利<br>进<br>行<br>中")
        
    def reset_clicked(self):
        self.main_timer.stop()
        self.main_time_left = 420
        self.main_timer_label.setText("07:00")
        self.game_status.setText("等待比赛中...")
        self.red_team_status.setText("等<br>待<br>中")
        self.blue_team_status.setText("等<br>待<br>中")
        
    def update(self):
        self.main_time_left -= 1
        if self.main_time_left >= 0:
            minutes = self.main_time_left // 60
            seconds = self.main_time_left % 60
            self.main_timer_label.setText("{:02d}:{:02d}".format(minutes, seconds))
        else:
            self.main_timer.stop()
            self.main_timer_label.setText("00:00")
            self.red_team_status.setText("等<br>待<br>中")
            self.blue_team_status.setText("等<br>待<br>中")
            self.game_status.setText("比赛结束")
        
    def __init__(self):
        super().__init__()
        self.InitUI()
        
    def keyPressEvent(self, envent):
        key = envent.key()
        if key == Qt.Key_Escape or key == Qt.Key_Q:
            self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showFullScreen()
    mainWindow.show()
    sys.exit(app.exec_())
    