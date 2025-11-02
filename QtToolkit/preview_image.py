"""
# Preview Image

* Disclaimer

    This is pretty old and originally written in PySide2, I don't think this is
    the best way to write this class today.

* Descriptions

    A UI component class that holds an updatable preview image and a label.
    Contains basic functionality for handling invalid paths.
"""


from pathlib import Path
from typing import Optional

from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets

import QtToolkit.gui


# TODO: Refactor this to work with image_sequence.ImageSequence

class PreviewImage(QtWidgets.QWidget):
    def __init__(self, label: str, size: tuple[int, int] = None,
                 label_top: bool = True):
        super().__init__()
        if size is None:
            self.size = [200, 200]
        else:
            self.size = size

        self.layout_main = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout_main)

        self.image_path: Path = Path('/does/not/exist')
        self.DEFAULT_IMAGE_PATH = Path(QtToolkit.icons.ICON_NO_PREVIEW_384x384)

        self.label = QtWidgets.QLabel(label)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image = QtWidgets.QLabel()

        if label_top:
            if label:  # no reason to add label if it contains no text
                self.layout_main.addWidget(self.label)
            self.layout_main.addWidget(self.image)
        else:
            self.layout_main.addWidget(self.image)
            if label:  # no reason to add label if it contains no text
                self.layout_main.addWidget(self.label)

        self.update_preview()

    def update_preview(self, image_path: Optional[Path] = None):
        """
        Updates and resets the pixmap to display the asset screenshot.

        Args:
            image_path (Optional[Path]): The file path to the image. If None is
             given, the preview will be set to the default image path.

        Returns:
            list: A list of strings containing the version entries. If not
             versions exist, an empty list will be returned.
        """
        if image_path is None or not image_path.exists():
            image_path = self.DEFAULT_IMAGE_PATH

        self.pixmap_preview = QtGui.QPixmap(image_path.as_posix())
        self.pixmap_preview = self.pixmap_preview.scaled(self.size[0],
                                                         self.size[1],
                                                         QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                                         QtCore.Qt.TransformationMode.FastTransformation)
        self.image.setPixmap(self.pixmap_preview)

    def set_pixmap(self, pixmap: QtGui.QPixmap) -> None:
        """Sets the pixmap of the image."""
        self.image.setPixmap(pixmap)
