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

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)

        self.tabs.tabBarDoubleClicked.connect(lambda index: self.newTabMethod())
        self.tabs.currentChanged.connect(self.currentTabChanged)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closedCurrentTab)

        self.newTabMethod()

        layout = QGridLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        layout.addWidget(self.inputBar, 0, 3)
        layout.addWidget(self.previousButton, 0, 0)
        layout.addWidget(self.forwardButton, 0, 1)

        layout.addWidget(self.tabs, 1, 0, 1, 4)
        
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
        
    def newTabMethod(self, url = None, label = "Blank"):
        if url is None:
            url = QUrl('https://www.google.com')

        browser = QWebEngineView()

        browser.setUrl(url)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda url, browser = browser: self.update_urlBar(url, browser))
        browser.loadFinished.connect(lambda _, i = i, browser = browser: self.tabs.setTabText(i, browser.page().title()))
    
    def currentTabChanged(self, i):
        url = self.tabs.currentWidget().url()
        self.update_urlBar(url, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def closedCurrentTab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)
    
    def update_title(self, browser) :
        if browser != self.tabs.currentWidget():
            return
        
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - Geek PyQt5" % title)
    
    def update_urlBar(self, q, browser = None):
        if browser != self.tabs.currentWidget():
            return
        self.inputBar.setText(q.toString())
        self.inputBar.setCursorPosition(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = browser()
    window.show()
    sys.exit(app.exec_())
