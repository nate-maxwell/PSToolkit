"""
# Dictionary Viewer

* Description:

    A menu that displays keys and values of a dictionary, recursively
    generating for nested dictionaries.
"""

from collections.abc import Mapping

from PySide6 import QtWidgets

from PSToolkit import shapes
from PSToolkit.groupbox import GroupBox


class DictViewer(GroupBox):
    def __init__(self,
                 menu_title: str,
                 data: Mapping,
                 default_closed: bool = False) -> None:
        super().__init__(menu_title, True)
        self.default_closed = default_closed
        self.setMinimumWidth(250)
        self.data = data
        self.refresh()
        self.add_stretch()
        if self.default_closed:
            self.setChecked(False)

    def refresh(self) -> None:
        """Redraws the menu from self.data."""
        self.clear()
        self._refresh(self.data)

    def _refresh(self, data: Mapping) -> None:
        """Recursive call for refreshing.
        Data values could be nested dictionaries.
        Keys are cast to str and single row value are cast to str, while dict
        values are kept the same.
        """
        for k, v in data.items():
            self.add_widget(shapes.HorizontalLine())
            if isinstance(v, Mapping):
                self._add_row_dict(str(k), v)
            else:
                self._add_row_str(str(k), str(v))

    def _add_row_dict(self, label: str, data: Mapping) -> None:
        """Adds a nested DictViewer if the value of the instanced data var
        was another dictionary.
        """
        wid_value = DictViewer(label, data, False)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.setContentsMargins(1, 1, 1, 1)
        hlayout.addWidget(wid_value)

        self.add_layout(hlayout)

    def _add_row_str(self, label: str, value: str) -> None:
        """Adds a row with a label and read-only line edit containing a str()
        version of the given value.
        """
        lbl_key = QtWidgets.QLabel(label)
        lbl_key.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                              QtWidgets.QSizePolicy.Policy.Preferred)

        lbl_value = QtWidgets.QLineEdit(str(value))
        lbl_value.setReadOnly(True)
        lbl_value.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                QtWidgets.QSizePolicy.Policy.Preferred)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.setContentsMargins(1, 1, 1, 1)
        hlayout.addWidget(lbl_key)
        hlayout.addWidget(lbl_value)

        self.add_layout(hlayout)
