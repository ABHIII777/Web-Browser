import PyQt5, sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("BROWSER")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.inputBar = QLineEdit()
        self.inputBar.returnPressed.connect(self.navigationMethod)

        self.previousButton = QPushButton("Back")
        self.previousButton.clicked.connect(self.previousPageMethod)
        self.previousButton.setFixedSize(60, 30)

        self.forwardButton = QPushButton("Forth")
        self.forwardButton.clicked.connect(self.forthPageMethod)
        self.forwardButton.setFixedSize(60, 30)

        self.newTabButton = QPushButton("Add")
        self.newTabButton.setFixedSize(60, 30)
        self.newTabButton.clicked.connect(self.newTabMethod)

        layout = QGridLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        layout.addWidget(self.inputBar, 0, 3)
        layout.addWidget(self.previousButton, 0, 0)
        layout.addWidget(self.forwardButton, 0, 1)
        layout.addWidget(self.newTabButton, 0, 2)
        
        layout.addWidget(self.browser, 3, 0, 1, 4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigationMethod(self):
        text = self.inputBar.text()
        if not text.startswith("http://"):
            text = "http://" + text

        self.browser.setUrl(QUrl(text))
    
    def previousPageMethod(self):
        if self.browser.history().canGoBack():
            self.browser.back()
    
    def forthPageMethod(self):
        if self.browser.history().canGoForward():
            self.browser.forward()
        
    def newTabMethod(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = browser()
    window.show()
    sys.exit(app.exec_())
