import PyQt5, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setting up main window
        
        self.setWindowTitle("BROWSER")
        self.setGeometry(100, 100, 1200, 800)

        #  Web Engine and URL bar

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.inputBar = QLineEdit()
        self.inputBar.returnPressed.connect(self.navigationMethod)

        # Navigation buttons

        self.navigationButton = QPushButton("navigate")
        self.navigationButton.clicked.connect(self.navigationMethod)
        
        # Layout setup
        
        layout = QVBoxLayout()
        layout.addWidget(self.inputBar)
        layout.addWidget(self.navigationButton)
        layout.addWidget(self.browser)

        # Central Widget
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        
        # Navigation Method

    def navigationMethod(self):
        text = self.inputBar.text()
        if not text.startswith("http://"):
            text = "http://" + text

        self.browser.setUrl(QUrl(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = browser()
    window.show()
    sys.exit(app.exec_())
