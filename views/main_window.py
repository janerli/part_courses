from PyQt6.QtWidgets import *

from tabs.catalog_tab import CatalogTab
from tabs.my_courses_tab import MyCoursesTab


class MainWindow(QMainWindow):
    def __init__(self, user_data, db):
        super().__init__()
        self.user = user_data
        self.db = db
        self.setWindowTitle(f"Онлайн-школа | {self.user['full_name']} | {self.user['role']}")
        self.resize(1000, 700)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        self.tabs.addTab(CatalogTab(self.user, self.db), "Каталог курсов")

        if self.user["role"] in ('student', 'teacher'):
            self.tabs.addTab(MyCoursesTab(self.user, self.db), "Мои курсы")

        btn_logout = QPushButton("Выход")
        btn_logout.clicked.connect(self.close)
        main_layout.addWidget(btn_logout)