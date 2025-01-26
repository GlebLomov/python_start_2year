import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow

# M4Y4
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
from PIL import ImageEnhance


class EasyEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Змінна для зберігання поточної робочої директорії
        self.workdir = ''
        # M4Y4
        self.workimage = ImageProcessor(self.ui)
        

        # Підключаємо сигнали до кнопок
        self.ui.btn_dir.clicked.connect(self.show_filenames_list)
        # M4Y4
        self.ui.btn_bw.clicked.connect(self.workimage.do_bw)  # Підключаємо обробник чорно-білого зображення
        self.ui.lw_files.currentRowChanged.connect(self.showChosenImage)
        
        # M4Y5
        self.ui.btn_left.clicked.connect(self.workimage.do_left)
        self.ui.btn_right.clicked.connect(self.workimage.do_right)
        self.ui.btn_sharp.clicked.connect(self.workimage.do_sharpen)
        self.ui.btn_flip.clicked.connect(self.workimage.do_flip)
        
        # self.ui.btn_blur.clicked.connect(self.workimage.do_blur) # додаткове завдання
        # self.ui.btn_bright.clicked.connect(self.workimage.do_brightness) # додаткове завдання

        

    """
    Фільтрує файли в заданій директорії за розширенням (png, jpg etc).
    """
    def filter(self, files, extensions):
        # return [filename for filename in files if any(filename.endswith(ext) for ext in extensions)]
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result


    """
    Відкриває діалог вибору директорії та зберігає її шлях.
    """
    def choose_workdir(self):
        self.workdir = QFileDialog.getExistingDirectory(self, "Обрати папку")
        # M4Y5
        self.workimage.save_workdir(self.workdir)
    
    
    """
    Показує список зображень в обраній директорії.
    """
    def show_filenames_list(self):
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        self.choose_workdir()
        if self.workdir:
            filenames = self.filter(os.listdir(self.workdir), extensions)
            self.ui.lw_files.clear()
            self.ui.lw_files.addItems(filenames)
    
    """
    Відображає вибране зображення
    """
    def showChosenImage(self):
        if self.ui.lw_files.currentRow() >= 0:
            filename = self.ui.lw_files.currentItem().text()
            self.workimage.loadImage(self.workdir, filename)
            image_path = os.path.join(self.workimage.dir, self.workimage.filename)
            self.workimage.showImage(image_path)

# M4Y4
class ImageProcessor:
    def __init__(self, ui):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.ui = ui  # Передаємо інтерфейс для доступу до елементів


    ''' Запам'ятовуємо шлях та ім'я файлу, завантажуємо зображення '''
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    ''' Конвертуємо зображення в чорно-біле '''
    def do_bw(self):
        if self.image:
            self.image = self.image.convert("L")
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)

    ''' Зберігає копію файлу в підпапці '''
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not os.path.exists(path):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    '''' Відображає зображення в інтерфейсі '''
    def showImage(self, path):
        self.ui.lb_image.hide()
        pixmap = QPixmap(path)
        w, h = self.ui.lb_image.width(), self.ui.lb_image.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.lb_image.setPixmap(pixmap)
        self.ui.lb_image.show()
        
        
    # M4Y5
    def save_workdir(self, workdir):
        self.workdir = workdir
        
    def do_left(self):
       self.image = self.image.transpose(Image.ROTATE_90)
       self.saveImage()
       image_path = os.path.join(self.workdir, self.save_dir, self.filename)
       self.showImage(image_path)
 
    def do_right(self):
       self.image = self.image.transpose(Image.ROTATE_270)
       self.saveImage()
       image_path = os.path.join(self.workdir, self.save_dir, self.filename)
       self.showImage(image_path)
 
    def do_flip(self):
       self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
       self.saveImage()
       image_path = os.path.join(self.workdir, self.save_dir, self.filename)
       self.showImage(image_path)

    def do_sharpen(self):
       self.image = self.image.filter(ImageFilter.SHARPEN)
       self.saveImage()
       image_path = os.path.join(self.workdir, self.save_dir, self.filename)
       self.showImage(image_path)

    # розмиття: додаткове завдання
    def do_blur(self):
       self.image = self.image.filter(ImageFilter.GaussianBlur(5))
       self.saveImage()
       image_path = os.path.join(self.workdir, self.save_dir, self.filename)
       self.showImage(image_path)
    
    # яскравість: додаткове завдання
    def do_brightness(self):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(1.5)
        self.saveImage()
        image_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.showImage(image_path)
       
       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = EasyEditor()
    main_window.show()
    sys.exit(app.exec())
