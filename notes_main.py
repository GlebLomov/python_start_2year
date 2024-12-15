from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtCore import Qt
import json
from ui import Ui_MainWindow

app = QApplication([])

# Створюємо головне вікно та інтерфейс
class NotesApp:
    def __init__(self):
        self.main_window = QMainWindow()  # Екземпляр QMainWindow
        self.ui = Ui_MainWindow()         # Інтерфейс
        self.ui.setupUi(self.main_window)  # Конектимо інтерфейс до QMainWindow
        
        self.notes = {}
        self.setup_ui()
        self.load_notes()
        
    def setup_ui(self):
        # Події для натиску на кнопки
        self.ui.button_note_create.clicked.connect(self.add_note)
        self.ui.button_note_del.clicked.connect(self.del_note)
        self.ui.button_note_save.clicked.connect(self.save_note)
        self.ui.button_tag_add.clicked.connect(self.add_tag)
        self.ui.button_tag_del.clicked.connect(self.del_tag)
        self.ui.button_tag_search.clicked.connect(self.search_tag)
        self.ui.listWidget.itemClicked.connect(self.show_note)
    
    def load_notes(self):
        try:
            with open("notes_data.json", "r") as file:
                self.notes = json.load(file)
            self.ui.listWidget.addItems(self.notes)
        except FileNotFoundError:
            self.notes = {}
    
    ''' Функционал програми'''
    def add_note(self):
        note_name, ok = QInputDialog.getText(self.main_window, "Додати замітку", "Назва замітки:")
        if ok and note_name != "":
            self.notes[note_name] = {"текст": "", "теги": []}
            self.ui.listWidget.addItem(note_name)
            print(self.notes)

    def show_note(self):
        key = self.ui.listWidget.selectedItems()[0].text()
        self.ui.field_text.setText(self.notes[key]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[key]["теги"])

    def save_note(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            self.notes[key]["текст"] = self.ui.field_text.toPlainText()
            with open("notes_data.json", "w") as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
            print(self.notes)
        else:
            print("Замітка для збереження не вибрана!")

    def del_note(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            del self.notes[key]
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.field_text.clear()
            self.ui.listWidget.addItems(self.notes)
            with open("notes_data.json", "w") as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
            print(self.notes)
        else:
            print("Замітка для вилучення не обрана!")

    def add_tag(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            tag = self.ui.field_tag.text()
            if tag not in self.notes[key]["теги"]:
                self.notes[key]["теги"].append(tag)
                self.ui.listWidget_2.addItem(tag)
                self.ui.field_tag.clear()
                with open("notes_data.json", "w") as file:
                    json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
            print(self.notes)
        else:
            print("Замітка для додавання тега не обрана!")

    def del_tag(self):
        if self.ui.listWidget_2.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            tag = self.ui.listWidget_2.selectedItems()[0].text()
            self.notes[key]["теги"].remove(tag)
            self.ui.listWidget_2.clear()
            self.ui.listWidget_2.addItems(self.notes[key]["теги"])
            with open("notes_data.json", "w") as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
        else:
            print("Тег для вилучення не обраний!")

    def search_tag(self):
        tag = self.ui.field_tag.text()
        if self.ui.button_tag_search.text() == "Шукати замітки за тегом" and tag:
            notes_filtered = {note: data for note, data in self.notes.items() if tag in data["теги"]}
            self.ui.button_tag_search.setText("Скинути пошук")
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(notes_filtered)
        elif self.ui.button_tag_search.text() == "Скинути пошук":
            self.ui.field_tag.clear()
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.notes)
            self.ui.button_tag_search.setText("Шукати замітки за тегом")

# Запуск
if __name__ == '__main__':
    main_app = NotesApp()
    main_app.main_window.show()
    app.exec_()
