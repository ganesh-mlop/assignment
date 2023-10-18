import sys
import sqlite3
import bcrypt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('User Login')
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Connect to the SQLite database
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()

        # Retrieve the stored hashed password for the given username
        cursor.execute('SELECT username, password FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        
        if user:
            stored_password = user[1]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                # Successful login; you can open the main application window here.
                print('Login successful!')
            else:
                # Failed login; show an error message.
                print('Login failed. Please check your credentials.')
        else:
            print('User does not exist.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
