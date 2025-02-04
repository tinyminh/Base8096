import base64
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget

class Base8096Encoder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base8096 Encoder/Decoder")
        self.setGeometry(100, 100, 600, 400)

        # Create Widgets
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText("Enter text to encode")
        
        self.encoded_output = QTextEdit(self)
        self.encoded_output.setPlaceholderText("Encoded output")
        self.encoded_output.setReadOnly(True)
        
        self.decode_input = QTextEdit(self)
        self.decode_input.setPlaceholderText("Enter text to decode")
        
        self.decoded_output = QTextEdit(self)
        self.decoded_output.setPlaceholderText("Decoded output")
        self.decoded_output.setReadOnly(True)
        
        # Buttons for Encode and Decode
        self.encode_button = QPushButton("Encode", self)
        self.decode_button = QPushButton("Decode", self)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_text)
        layout.addWidget(self.encode_button)
        layout.addWidget(self.encoded_output)
        layout.addWidget(self.decode_input)
        layout.addWidget(self.decode_button)
        layout.addWidget(self.decoded_output)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Connect Buttons
        self.encode_button.clicked.connect(self.encode_text)
        self.decode_button.clicked.connect(self.decode_text)
    
    def encode_text(self):
        text = self.input_text.toPlainText()
        if text:
            # Custom encoding logic (you can replace this with Base8096 logic)
            encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            self.encoded_output.setPlainText(encoded_text)
    
    def decode_text(self):
        encoded_text = self.decode_input.toPlainText()
        if encoded_text:
            try:
                # Custom decoding logic (you can replace this with Base8096 logic)
                decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
                self.decoded_output.setPlainText(decoded_text)
            except Exception as e:
                self.decoded_output.setPlainText("Error decoding: " + str(e))


if __name__ == '__main__':
    app = QApplication([])
    window = Base8096Encoder()
    window.show()
    app.exec()
