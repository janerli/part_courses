from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from widgets.course_page import CoursePage


class MyCoursesTab(QWidget):
    def __init__(self, user_data, db):
        super().__init__()
        self.user_data = user_data
        self.db = db
        self.setup_ui()
        self.load_my_courses()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("{border: none;}")
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.scroll_widget)
        layout.addWidget(self.scroll_area)

    def load_my_courses(self):
        if self.user_data['role'] == 'student':
            courses = self.db.fetchall("""
            select *
            from enrollments e 
            join courses c on c.course_id = e.course_id
            join users u on u.user_id = e.student_id
            where e.student_id=%s""", (self.user_data['user_id'],))
        elif self.user_data['role'] == 'teacher':
            courses = self.db.fetchall("""
            select *
            from enrollments e 
            join courses c on c.course_id = e.course_id
            join users u on u.user_id = c.teacher_id
            where u.user_id=%s""", (self.user_data['user_id'],))
        print(courses)

        self.clear_layout(self.scroll_layout)

        for course in courses:
            card = self.create_card(course)
            self.scroll_layout.addWidget(card)

    def create_card(self, course):
        print(course)
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setStyleSheet("{border: none;}")
        card.setMaximumSize(1000, 100)

        card_layout = QGridLayout(card)
        card_layout.setSpacing(10)
        card_layout.addWidget(QLabel(f"{course['title']}"), 0, 0)
        go_btn = QPushButton("Перейти на страницу курса")
        go_btn.clicked.connect(lambda checked, p=course: self.go_to_course_page(p))
        card_layout.addWidget(go_btn, 0, 1)
        return card

    def go_to_course_page(self, course):
        widget = CoursePage(self.user_data, self.db, course, parent=self)
        widget.exec()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
