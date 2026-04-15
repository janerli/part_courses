import sys
from PyQt6.QtWidgets import QApplication
from database import db
from views.login_window import LoginDialog
from views.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    db.connect()
    dlg = LoginDialog(db)
    if dlg.exec() == 1:
        user = dlg.get_user()
        window = MainWindow(user, db)
        window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()