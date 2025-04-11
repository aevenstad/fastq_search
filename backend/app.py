from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import subprocess
import sys
from threading import Thread
import os

# Set the QT_QPA_PLATFORM environment variable to offscreen to run the app without a display
os.environ["QT_QPA_PLATFORM"] = "offscreen"

# Function to start Flask server in the background
def start_flask():
    copy_fastq_script = os.path.join(os.path.dirname(__file__), "copy_fastq.py")
    subprocess.run(["python3", copy_fastq_script])

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Locator App")
        self.setGeometry(100, 100, 800, 600)

        web_view = QWebEngineView()
        web_view.setUrl(QUrl("http://127.0.0.1:5000"))  # Flask app URL

        layout = QVBoxLayout()
        layout.addWidget(web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    # Start Flask server in a separate thread
    flask_thread = Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Launch the PyQt5 desktop app
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())