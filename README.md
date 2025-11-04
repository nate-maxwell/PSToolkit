# PSToolkit
A library of PySide helpers + stylesheets specifically for Windows development.

Currently, PySide 6 compatible.

### Stylesheet Viewer

Run `PSToolkit._example.style_viewer` file itself, to see an example widget
that displays all the collected style sheets.

<img src="https://i.imgur.com/DePm39f.png">

### Wrappers

Wrapper methods will always be snake_case, i.e. if a widget has methods to
add widgets or layouts, it will be `widget.add_widget(wid)`,
`layout.add_stretch()`, or `widget.add_layout(lay)`, which will be shorthand
for `widget.layout.addWidget(wid)`, etc. If those methods are not present, the
wrappers do not exist for that class.

Properties are not used to keep the workflow / coding style similar to actual
PySide. Use `object.value()` or  `object.get_value()` and 
`object.set_value(val)`.

### Resources

`QtToolkit.gui` contains path variables to the stored icons and stylesheets.
*/.idea
