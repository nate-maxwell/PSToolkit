"""
# Labeled Line Edit

* Descriptions

    A UI component class that is a label and a line edit. This is mostly
    for eliminating boilerplate for tools that have a labeled row that
    contains a line edit.
"""


from PySide6 import QtWidgets


class LabeledLineEdit(QtWidgets.QWidget):
    """A composite widget combining a label and a line edit.

    This class creates a labeled text input field arranged either
    horizontally (label to the left) or vertically (label above). It is
    intended for use in form-like UIs or tool panels where clear labeling
    of user input fields is required.

    Example:
        >>> name_field = LabeledLineEdit('Name:')
        >>> name_field.set_placeholder_text('Enter your name')
        >>> print(name_field.text())

    Attributes:
        layout_main (QtWidgets.QLayout): The main layout managing the label
            and line edit widgets, set to ``QHBoxLayout`` or ``QVBoxLayout``
            depending on the ``vertical`` argument.
        label (QtWidgets.QLabel): The descriptive label displayed next to or
            above the line edit.
        line_edit (QtWidgets.QLineEdit): The editable text input field.

    Args:
        text (str): The label text displayed beside or above the input field.
        vertical (bool): If ``True``, the label appears above the line edit
            (vertical layout); otherwise, the label appears to the left
            (horizontal layout). Defaults to ``False``.
    """

    def __init__(self, text: str, vertical: bool = False) -> None:
        super().__init__()
        if vertical:
            self.layout_main = QtWidgets.QVBoxLayout()
        else:
            self.layout_main = QtWidgets.QHBoxLayout()

        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_main)
        self.label = QtWidgets.QLabel(text)
        self.line_edit = QtWidgets.QLineEdit()
        self.layout_main.addWidget(self.label)
        self.layout_main.addWidget(self.line_edit)

    def text(self) -> str:
        """Returns the current line edit text."""
        return self.line_edit.text()

    def set_text(self, s: str) -> None:
        """Sets the text of the line edit."""
        self.line_edit.setText(s)

    def set_placeholder_text(self, s: str) -> None:
        """Sets the placeholder text of the line edit."""
        self.line_edit.setPlaceholderText(s)

    def clear(self) -> None:
        """Shortened namespace to clear text."""
        self.line_edit.clear()
