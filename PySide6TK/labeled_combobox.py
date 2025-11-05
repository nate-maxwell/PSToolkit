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
    """A composite widget combining a label and a combo box.

    This class provides a labeled drop-down selection field with optional
    support for dynamically adding new items. The layout can be horizontal
    or vertical, depending on the use case. It simplifies UI construction
    for settings panels, tool dialogs, and configurable parameter groups.

    Example:
        >>> quality_box = LabeledComboBox('Quality', ['Low', 'Medium', 'High'])
        >>> print(quality_box.current_text())

        >>> appendable_box = LabeledComboBox('Category', appendable=True)
        >>> appendable_box.append_item()  # Prompts user to add a new entry

    Attributes:
        layout_main (QtWidgets.QLayout): The main layout managing the label,
            combo box, and optional add button. Uses either ``QHBoxLayout``
            or ``QVBoxLayout`` depending on the ``vertical`` argument.
        label (QtWidgets.QLabel): The descriptive label displayed next to or
            above the combo box.
        cmb_box (QtWidgets.QComboBox): The drop-down selection widget.
        btn_add (Optional[QtWidgets.QPushButton]): Optional “+” button for
            appending new combo box entries when ``appendable`` is ``True``.

    Args:
        text (str): The label text displayed beside or above the combo box.
        contents (Optional[list[str]]): The initial list of items to populate
            the combo box with. Defaults to ``None``.
        appendable (bool): If ``True``, adds a “+” button allowing users to
            append new items interactively via a text dialog. Defaults to
            ``False``.
        vertical (bool): If ``True``, places the label above the combo box
            (vertical layout); otherwise, beside it (horizontal layout).
            Defaults to ``False``.

    Notes:
        - The combo box automatically resizes horizontally to fill available
          space.
        - When ``appendable`` is enabled, new items are sorted alphabetically
          after being added.
    """

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
