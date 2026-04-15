from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class CatalogTab(QWidget):
    def __init__(self, user_data, db):
        super().__init__()
        self.user = user_data
        self.db = db
        self.setup_ui()
        self.load_catalog()

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

    def load_catalog(self):
        courses = self.db.fetchall("select * from courses")

        self.clear_layout(self.scroll_layout)

        for course in courses:
            card = self.create_card(course)
            self.scroll_layout.addWidget(card)

    def create_card(self, course):
        print(course)
        card = QFrame()
        card.setFrameShape(QFrame.Shape.Box)
        card.setMaximumSize(1000, 100)

        card_layout = QGridLayout(card)
        card_layout.setSpacing(10)
        teacher = self.db.fetchone("select * from users where user_id=%s", (course['teacher_id']))
        print(teacher)
        card_layout.addWidget(QLabel(f'Название: {course["title"]}'), 0, 0)
        card_layout.addWidget(QLabel(f"Преподаватель: {teacher['full_name']}"), 1, 0)
        card_layout.addWidget(QLabel(f"Цена: {course['price']:,.0f} руб."), 2, 0)

        go_btn = QPushButton("Записаться")
        go_btn.clicked.connect(lambda checked, p=course: self.go_to_course(p))
        card_layout.addWidget(go_btn, 0, 1)
        return card

    def go_to_course(self, course):
        reply = QMessageBox.question(self, "Запись на курс", "Вы уверены что хотите записаться?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.db.execute("""
            insert into enrollments(student_id, course_id, status)
            values (%s, %s, %s)""", (course['student_id'], course['course_id'], "активна"))
            QMessageBox.information(self, "Успех", "Вы успешно записались на курс!")
            

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()


