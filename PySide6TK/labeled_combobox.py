"""
# Labeled Combo Box

* Descriptions

    A UI component class that is a label and a combobox. This is mostly
    for eliminating boilerplate for tools that have a labeled row that
    contains a combobox.
"""

from typing import Optional

from PySide6 import QtCore
from PySide6 import QtWidgets

import PySide6TK.regx
import PySide6TK.dialogs


class LabeledComboBox(QtWidgets.QWidget):
    def __init__(self, text: str, contents: Optional[list[str]] = None,
                 appendable: bool = False, vertical: bool = False) -> None:
        super().__init__()
        if vertical:
            self.layout_main = QtWidgets.QVBoxLayout()
        else:
            self.layout_main = QtWidgets.QHBoxLayout()

        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_main)
        self.label = QtWidgets.QLabel(text)
        self.layout_main.addWidget(self.label)
        self.cmb_box = QtWidgets.QComboBox()
        self.cmb_box.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                   QtWidgets.QSizePolicy.Policy.Fixed)

        if contents:
            self.cmb_box.addItems(contents)
        self.layout_main.addWidget(self.cmb_box)

        if appendable:
            self.btn_add = QtWidgets.QPushButton('+')
            self.layout_main.addWidget(self.btn_add)
            self.btn_add.clicked.connect(self.append_item)

    def current_text(self) -> str:
        """Shortened namespace way to get current selected item."""
        return self.cmb_box.currentText()

    def item_is_alphanum(self) -> bool:
        """Returns whether the current item does not contain non-alpha-numeric
        or non-underscore characters.
        """
        return PySide6TK.regx.validation_no_special_chars(
            self.cmb_box.currentText())

    def clear(self) -> None:
        """Shortened namespace way to clear items."""
        self.cmb_box.clear()

    def add_items(self, items: list[str] = None):
        """Adds items much like QtWidgets.QComboBox.addItems()."""
        if items is None:
            return
        self.cmb_box.addItems(items)

    def append_item(self) -> None:
        dlg = PySide6TK.dialogs.SingleLineTextDialog('New Item', 'Name:')
        if dlg.exec():
            self.add_items([dlg.text()])
            self.cmb_box.model().sort(0, QtCore.Qt.SortOrder.AscendingOrder)

    def set_current_index(self, index: int):
        """Sets the combobox active index much like
        QtWidgets.QComboBox.setCurrentIndex().
        """
        self.cmb_box.setCurrentIndex(index)
