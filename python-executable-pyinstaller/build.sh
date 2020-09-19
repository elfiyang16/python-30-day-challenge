source bin/activate
pyinstaller src/wsgi.py -F \ #-F turn into single file execution
--name "cfe-os-mac" \
--icon='icon.icns' \
--add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' \ #add binary framework
--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' \
--add-data "src/data/*:data" \
--add-data "src/data/*.jpg:data" \
--hidden-import waitress \
--clean