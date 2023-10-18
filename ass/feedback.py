import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox

import application_window

class FeedbackForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('User Feedback')
        self.setGeometry(100, 100, 400, 300)

        self.feedback_label = QLabel('Provide Your Feedback:')
        self.feedback_input = QTextEdit()

        self.submit_button = QPushButton('Submit Feedback')
        self.submit_button.clicked.connect(self.submit_feedback)

        layout = QVBoxLayout()
        layout.addWidget(self.feedback_label)
        layout.addWidget(self.feedback_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_feedback(self):
        feedback = self.feedback_input.toPlainText()

        if not feedback:
            self.show_message('Please enter your feedback.')
        else:
            # You can store or process the feedback data as needed.
            self.show_message('Feedback submitted successfully.')

    def show_message(self, message):
        message_box = QMessageBox(self)
        message_box.setText(message)
        message_box.exec()


if __name__ == "__main__":
    app = application_window(sys.argv)
    window = FeedbackForm()
    window.show()
    sys.exit(app.exec_())

