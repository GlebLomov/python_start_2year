import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.configure()
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.video)
        self.get_date()

    def configure(self):
        self.ui.start.clicked.connect(self.media_play)
        self.ui.stop.clicked.connect(self.media_stop)
        self.ui.calendar.selectionChanged.connect(self.get_date)

    def get_date(self):
        self.media_stop()
        # print(self.ui.calendar.selectedDate())
        day = str(self.ui.calendar.selectedDate().day())
        file_path = f'Video\\{day}.avi'
        # file_path = f'python_start_2y/m4y1/Video/{day}.avi'


        if not os.path.exists(file_path):
            print(f"Файл не знайдено: {file_path}")
        else:
            self.media.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            print(f"Файл знайдено: {file_path}")
        if self.ui.autostart.isChecked():
            self.media_play()


    def media_play(self):
        self.media.play()

    def media_stop(self):
        self.media.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
