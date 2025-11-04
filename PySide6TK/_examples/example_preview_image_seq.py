
from pathlib import Path

import PySide6TK.app
import PySide6TK.main_window
from PySide6TK.preview_sequence import PreviewSequence


_FRAMES_PATH = Path(Path(__file__).parent, 'frames')

# Doubles as the example for preview_image.
# Minimal example - Probably should expand to have FPS combo box ¯\_(ツ)_/¯


class ExampleWindow(PySide6TK.main_window.MainWindow):
    def __init__(self) -> None:
        super().__init__('Example Preview Sequence')
        self.wid = PreviewSequence('Example Frames')
        self.wid.set_source(Path(_FRAMES_PATH))
        self.setCentralWidget(self.wid)


if __name__ == '__main__':
    PySide6TK.app.exec_app(ExampleWindow, 'ExampleSeqViewer')
