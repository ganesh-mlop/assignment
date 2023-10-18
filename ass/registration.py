import sys
import sqlite3
import bcrypt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QDialog, QFormLayout, QMainWindow, QAction, QMenuBar,  QMessageBox 
)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

# Create a shared SQLite connection
connection = sqlite3.connect('user_database.db')

class RegistrationWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('User Registration')
        self.setGeometry(100, 100, 300, 220)

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Enter username')

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Enter password')
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel('Confirm Password:')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText('Confirm password')
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton('Register')
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not password or not confirm_password:
            self.show_message('Please fill in all fields.')
            return

        if password != confirm_password:
            self.show_message('Passwords do not match.')
            return

        # Check if the username is already taken
        cursor = connection.cursor()
        cursor.execute('SELECT username FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()
        cursor.close()

        if existing_user:
            self.show_message('Username already exists. Please choose another.')
            return

        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        cursor.close()

        self.show_message('Registration successful!')

    def show_message(self, message):
        message_box = QMessageBox(self)
        message_box.setText(message)
        message_box.exec()

class UserDetailsDialog(QDialog):
    def __init__(self, username):
        super().__init__()

        self.username = username

        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('User Details')
        self.setGeometry(100, 100, 300, 200)

        cursor = connection.cursor()
        cursor.execute('SELECT username FROM users WHERE username=?', (self.username,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            username_label = QLabel('Username:')
            username_display = QLabel(user[0])

            layout = QFormLayout()
            layout.addRow(username_label, username_display)

            update_button = QPushButton('Update Profile')
            update_button.clicked.connect(self.update_profile)
            layout.addWidget(update_button)

            self.setLayout(layout)
        else:
            self.show_message('User not found.')

    def update_profile(self):
        # Implement profile update functionality here
        self.show_message('Profile update functionality is not implemented yet.')

    def show_message(self, message):
        message_box = QMessageBox(self)
        message_box.setText(message)
        message_box.exec()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ApplicationWindow()
    main_window.show()
    sys.exit(app.exec())
