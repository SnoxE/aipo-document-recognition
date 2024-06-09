import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

# Main window class
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("AiPO Document Recognition")

        # Create a layout
        layout = QVBoxLayout()

        # Create a button and add it to the layout
        self.button = QPushButton("Click Me")
        layout.addWidget(self.button)

        # Connect the button click signal to the slot method
        self.button.clicked.connect(self.show_message)

        # Set the layout for the main window
        self.setLayout(layout)

    # Slot method to show a message box
    def show_message(self):
        QMessageBox.information(self, "Message", "Button clicked!")

# Main function
def main():
    # Create the application object
    app = QApplication(sys.argv)

    # Create an instance of the window
    window = MyWindow()

    # Show the window
    window.show()

    # Start the application's event loop
    sys.exit(app.exec_())

# Run the main function
if __name__ == "__main__":
    main()