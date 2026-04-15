from datetime import datetime

from PyQt6.QtWidgets import *

class GoToCourseDialog(QDialog):
    def __init__(self, user_data, db, lesson, parent):
        super().__init__(parent)
        self.user = user_data
        self.db = db
        self.lesson = lesson
        self.setModal(True)
        self.setWindowTitle("Запись на курс")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        self.answer = QTextEdit()
        form.addRow("Ответ", self.answer)
        submit_btn = QPushButton("Сдать ДЗ")
        submit_btn.clicked.connect(self.insert_homework)
        layout.addLayout(form)
        layout.addWidget(submit_btn)

    def insert_homework(self):
        answer = self.answer.toPlainText().strip()
        self.db.execute("insert into homeworks(lesson_id, student_id, answer_text, submitted_date) values (%s, %s, %s, %s)",
                        (self.lesson['lesson_id'], self.user['user_id'], answer, datetime.now()))
        QMessageBox.information(self, "Успех", "Ваш ответ отправлен на проверку")
        self.accept()

