"""from PyQt5.QtWidgets import QMainWindow, QAction, QMenuBar
# from registration import RegistrationWindow
from registration import RegistrationWindow  # Adjust the import path

from registration import UserDetailsDialog

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        registration_action = QAction('Register', self)
        registration_action.triggered.connect(self.open_registration)
        file_menu.addAction(registration_action)

        user_details_action = QAction('User Details', self)
        user_details_action.triggered.connect(self.open_user_details)
        file_menu.addAction(user_details_action)

    def open_registration(self):
        registration_window = RegistrationWindow()
        registration_window.exec()

    def open_user_details(self):
        user_details_dialog = UserDetailsDialog('user1')  # Replace 'user1' with the actual username
        user_details_dialog.exec()
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar
from registration import RegistrationWindow, UserDetailsDialog

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        registration_action = QAction('Register', self)
        registration_action.triggered.connect(self.open_registration)
        file_menu.addAction(registration_action)

        user_details_action = QAction('User Details', self)
        user_details_action.triggered.connect(self.open_user_details)
        file_menu.addAction(user_details_action)

    def open_registration(self):
        registration_window = RegistrationWindow()
        registration_window.exec()

    def open_user_details(self):
        user_details_dialog = UserDetailsDialog('user1')  # Replace 'user1' with the actual username
        user_details_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec_())
