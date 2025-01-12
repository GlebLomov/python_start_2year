import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow

class EasyEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Змінна для зберігання поточної робочої директорії
        self.workdir = ""

        self.ui.btn_dir.clicked.connect(self.show_filenames_list)

        # Підключаємо сигнали до кнопок

    
    """
    Фільтрує файли в заданій директорії за розширенням (png, jpg etc).
    """
    def filter(self, files, extensions):
        result = []
        for filename in  files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result
    



        
    
    """
    Відкриває діалог вибору директорії та зберігає її шлях.
    """
    def choose_workdir(self):
        self.workdir = QFileDialog.getExistingDirectory(self,"Обрати папку")
        # Дописати код (видалити pass)
        
        
        
    """
    Показує список зображень в обраній директорії.
    """
    def show_filenames_list(self):
        extensions = [".jpg",".jpeg",".png",".gif",".bmp"]
        self.choose_workdir()
        if self.workdir:
            filenames = self.filter(os.listdir(self.workdir),extensions)
            self.ui.lw_files.clear()
            self.ui.lw_files.addItems(filenames)

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = EasyEditor()
    main_window.show()
    sys.exit(app.exec())
