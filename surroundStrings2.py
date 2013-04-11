#! /usr/bin/env python

#------------------------------------------------------------------------------

__author__ = "stealthbrite"
__copyright__ = "Copyright 2012, stealthbrite"
__license__ = "LGPL"
__version__ = "0.1.0"
__email__ = "stealthbrite@gmail.com"
__status__ = "Beta"

#------------------------------------------------------------------------------

"""
Takes the input and manipulates it
either by surrounding each line with ' '
or append a ,
or fill up the line with 0000
"""

#------------------------------------------------------------------------------

import sys
from PySide import QtGui
from PySide import QtCore

#------------------------------------------------------------------------------


class inputWindow(QtGui.QMainWindow):

#------------------------------------------------------------------------------

    def __init__(self, win_parent=None):
        #Init the base class
        QtGui.QMainWindow.__init__(self, win_parent)
        self.create_widgets()

#------------------------------------------------------------------------------

    def create_widgets(self):
        #Widgets
        self.input_edit = QtGui.QPlainTextEdit()
        self.surround_button = QtGui.QPushButton("Surround with \' \'")
        self.append_comma_button = QtGui.QPushButton("Append ,")
        self.append_zero_button = QtGui.QPushButton("Append 0000")

        #connect signal
        QtCore.QObject.connect(self.surround_button, QtCore.SIGNAL("clicked()"), self.on_surround_clicked)

        QtCore.QObject.connect(self.append_comma_button, QtCore.SIGNAL("clicked()"), self.on_append_comma_clicked)

        QtCore.QObject.connect(self.append_zero_button, QtCore.SIGNAL("clicked()"), self.on_append_zero_clicked)

        #Horizontal layout
        h_box = QtGui.QHBoxLayout()
        h_box.addWidget(self.append_zero_button)
        h_box.addWidget(self.surround_button)
        h_box.addWidget(self.append_comma_button)

        #Vertical layout
        v_box = QtGui.QVBoxLayout()
        v_box.addWidget(self.input_edit)
        v_box.addLayout(h_box)

        #Create central widget, add layout and set
        central_widget = QtGui.QWidget()
        central_widget.setLayout(v_box)
        self.setCentralWidget(central_widget)

#------------------------------------------------------------------------------

    def on_surround_clicked(self):
        """
        Surrounds each Line of the inputField with "' '"
        """
        out = ''
        lines = str((self.input_edit.toPlainText())).splitlines()
        for line in lines:
            out = out + '\'' + line.strip() + '\'' + '\n'
        out = out.rstrip('\n')
        self.input_edit.setPlainText(out)

#------------------------------------------------------------------------------

    def on_append_comma_clicked(self):
        """
        Appends each Line, except for the last line, of the inputField with ","
        """
        out = ''
        lines = str((self.input_edit.toPlainText())).splitlines()
        for line in lines:
            out = out + line + ',' + '\n'
        out = out.rstrip(',\n')
        self.input_edit.setPlainText(out)

#------------------------------------------------------------------------------

    def on_append_zero_clicked(self):
        """
        Appends to each Line 4 Zeros.
        """
        out = ''
        lines = str((self.input_edit.toPlainText())).splitlines()
        for line in lines:
            out = out + line + '0000' + '\n'
        self.input_edit.setPlainText(out)

#------------------------------------------------------------------------------


def main():
    app = QtGui.QApplication(sys.argv)
    main_window = inputWindow()
    main_window.show()
    app.exec_()

#------------------------------------------------------------------------------

print "called ", __name__
if __name__ == '__main__':
    main()
