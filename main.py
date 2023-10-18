import sys
from PyQt5.QtWidgets import QApplication
from ass.application_window import ApplicationWindow
from ass.database import connection  

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ApplicationWindow(connection)  
    window.show()  
    sys.exit(app.exec_())

