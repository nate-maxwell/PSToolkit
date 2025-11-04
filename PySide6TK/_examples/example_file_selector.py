from PySide6TK import app
from PySide6TK.main_window import MainWindow
from PySide6TK.file_selector import FileSelector


class Foo(MainWindow):
    def __init__(self) -> None:
        super().__init__('file selector')
        self.wid = FileSelector('file')
        self.setCentralWidget(self.wid)


if __name__ == '__main__':
    app.exec_app(Foo, 'ExampleFileSelector')
