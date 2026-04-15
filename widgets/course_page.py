from PyQt6.QtWidgets import *

from widgets.go_to_course_dialog import GoToCourseDialog


class CoursePage(QDialog):
    def __init__(self, user_data, db, course, parent):
        super().__init__(parent)
        self.user_data = user_data
        self.db = db
        self.course = course
        self.setWindowTitle(f"Страница курса {course['title']}")
        self.setFixedSize(800, 600)
        self.setModal(True)
        self.setup_ui()
        self.load_course_page()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        self.lessons = QListWidget()
        layout.addWidget(self.lessons)
        if self.user_data['role'] == "student":
            st_btn = QPushButton("Сдать ДЗ")
            st_btn.clicked.connect(self.send_homework)
            layout.addWidget(st_btn)
        elif self.user_data['role'] == "teacher":
            tch_btn = QPushButton("Сдать ДЗ")
            tch_btn.clicked.connect(self.check_homework)
            layout.addWidget(tch_btn)

    def load_course_page(self):
        lesson = self.db.fetchall("select * from lessons where course_id=%s", (self.course['course_id']))
        for l in lesson:
            self.lessons.addItem(l['title'])


    def send_homework(self):
        lesn = self.db.fetchone("select * from lessons where title=%s", (self.lessons.currentItem().text().strip()))
        dlg = GoToCourseDialog(self.user_data, self.db, lesn, parent=self)
        dlg.exec()

    def check_homework(self):
        print("check homework")