from pathlib import Path
from typing import Union

from PySide6 import QtWidgets


QT_COMMON_TYPE = Union[QtWidgets.QWidget, QtWidgets.QLayout]
RESOURCES_PATH = Path(Path(__file__).parent, 'resources')
