from PyQt6.QtWidgets import *


class LoginDialog(QDialog):
    def __init__(self, db):
        super().__init__()
        self.user_data = None
        self.db = db
        self.setWindowTitle("Авторизация")
        self.setFixedSize(340, 220)
        self.setup_ui()

    def setup_ui(self):
        form = QVBoxLayout(self)
        layout = QFormLayout()

        self.username = QLineEdit()
        self.password = QLineEdit()
        layout.addRow("login", self.username)
        layout.addRow("password", self.password)

        auth_btn = QPushButton("Войти")
        guest_btn = QPushButton("Войти как гость")
        auth_btn.clicked.connect(self.auth)
        guest_btn.clicked.connect(self.guest_auth)
        form.addWidget(auth_btn)
        form.addWidget(guest_btn)
        form.addLayout(layout)

    def auth(self):
        username = self.username.text().strip()
        password = self.password.text().strip()

        user = self.db.fetchone("select * from users where username = %s and password = %s", (username,password))
        if user:
            role = self.db.fetchone("select role_name from roles where role_id = %s", (user['role_id']))
            self.user_data = {
                "user_id": user['user_id'],
                "username": user['username'],
                "role": role['role_name'],
                "full_name": user['full_name'],
                "email": user['email'],
            }

        self.accept()

    def guest_auth(self):
        self.user_data = {
            "user_id": '99999',
            "username": 'Гость',
            "role": 'guest',
            "full_name": "Гость"
        }
        self.accept()

    def get_user(self):
        return self.user_data