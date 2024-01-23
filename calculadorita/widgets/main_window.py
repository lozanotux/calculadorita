import calculadorita.constants as constants
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.math_opperation = ""
        self.result_entry = None
        
        self.add_css_class(constants.MAIN_WINDOW_DARK)

        # Main box to pack the rest of widgets
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        self.result_entry = Gtk.Entry()
        self.result_entry.set_can_focus(False)
        self.result_entry.set_has_frame(False)
        self.result_entry.set_editable(False)
        self.result_entry.set_text("0")
        self.result_entry.add_css_class(constants.RESULT_TEXT)
        self.result_entry.set_alignment(0.90)

        # Grid section
        self.grid = Gtk.Grid(
            column_spacing = 9,
            row_spacing = 9
        )
        self.grid.add_css_class(constants.MAIN_WINDOW_GRID)

        self.ac_button = Gtk.Button(label="AC")
        self.ac_button.add_css_class(constants.ACTION_BUTTON)
        # attach() -->(widget, column, row, width. height)
        self.grid.attach(self.ac_button, 0, 0, 3, 1)
        self.ac_button.connect('clicked', self.on_press_ac)

        self.seven_button = Gtk.Button(label="7")
        self.eight_button = Gtk.Button(label="8")
        self.nine_button = Gtk.Button(label="9")
        self.grid.attach(self.seven_button, 0, 1, 1, 1)
        self.grid.attach(self.eight_button, 1, 1, 1, 1)
        self.grid.attach(self.nine_button, 2, 1, 1, 1)
        self.seven_button.add_css_class(constants.NUMBER_BUTTON)
        self.eight_button.add_css_class(constants.NUMBER_BUTTON)
        self.nine_button.add_css_class(constants.NUMBER_BUTTON)
        self.seven_button.connect('clicked', self.on_press_7)
        self.eight_button.connect('clicked', self.on_press_8)
        self.nine_button.connect('clicked', self.on_press_9)

        self.four_button = Gtk.Button(label="4")
        self.five_button = Gtk.Button(label="5")
        self.six_button = Gtk.Button(label="6")
        self.grid.attach(self.four_button, 0, 2, 1, 1)
        self.grid.attach(self.five_button, 1, 2, 1, 1)
        self.grid.attach(self.six_button, 2, 2, 1, 1)
        self.four_button.add_css_class(constants.NUMBER_BUTTON)
        self.five_button.add_css_class(constants.NUMBER_BUTTON)
        self.six_button.add_css_class(constants.NUMBER_BUTTON)
        self.four_button.connect('clicked', self.on_press_4)
        self.five_button.connect('clicked', self.on_press_5)
        self.six_button.connect('clicked', self.on_press_6)

        self.one_button = Gtk.Button(label="1")
        self.two_button = Gtk.Button(label="2")
        self.three_button = Gtk.Button(label="3")
        self.grid.attach(self.one_button, 0, 3, 1, 1)
        self.grid.attach(self.two_button, 1, 3, 1, 1)
        self.grid.attach(self.three_button, 2, 3, 1, 1)
        self.one_button.add_css_class(constants.NUMBER_BUTTON)
        self.two_button.add_css_class(constants.NUMBER_BUTTON)
        self.three_button.add_css_class(constants.NUMBER_BUTTON)
        self.one_button.connect('clicked', self.on_press_1)
        self.two_button.connect('clicked', self.on_press_2)
        self.three_button.connect('clicked', self.on_press_3)

        self.zero_button = Gtk.Button(label="0")
        self.comma_button = Gtk.Button(label=",")
        self.grid.attach(self.zero_button, 0, 4, 2, 1)
        self.grid.attach(self.comma_button, 2, 4, 1, 1)
        self.zero_button.add_css_class(constants.ZERO_BUTTON)
        self.comma_button.add_css_class(constants.NUMBER_BUTTON)
        self.zero_button.connect('clicked', self.on_press_0)
        self.comma_button.connect('clicked', self.on_press_dot)

        self.divide_button = Gtk.Button(label="÷")
        self.multiply_button = Gtk.Button(label="×")
        self.subtract_button = Gtk.Button(label="−")
        self.sum_button = Gtk.Button(label="+")
        self.equal_button = Gtk.Button(label="=")
        self.grid.attach(self.divide_button, 3, 0, 1, 1)
        self.grid.attach(self.multiply_button, 3, 1, 1, 1)
        self.grid.attach(self.subtract_button, 3, 2, 1, 1)
        self.grid.attach(self.sum_button, 3, 3, 1, 1)
        self.grid.attach(self.equal_button, 3, 4, 1, 1)
        self.divide_button.add_css_class(constants.OPERATOR_BUTTON)
        self.multiply_button.add_css_class(constants.OPERATOR_BUTTON)
        self.subtract_button.add_css_class(constants.OPERATOR_BUTTON)
        self.sum_button.add_css_class(constants.OPERATOR_BUTTON)
        self.equal_button.add_css_class(constants.OPERATOR_BUTTON)
        self.divide_button.connect('clicked', self.on_press_divide)
        self.multiply_button.connect('clicked', self.on_press_multiply)
        self.subtract_button.connect('clicked', self.on_press_minus)
        self.sum_button.connect('clicked', self.on_press_plus)
        self.equal_button.connect('clicked', self.on_press_equal)

        self.main_box.append(self.result_entry)
        self.main_box.append(self.grid)
        self.set_child(self.main_box)

    def on_press_1(self, button):
        self.math_opperation += "1"
        self.result_entry.set_text(self.math_opperation)

    def on_press_2(self, button):
        self.math_opperation += "2"
        self.result_entry.set_text(self.math_opperation)

    def on_press_3(self, button):
        self.math_opperation += "3"
        self.result_entry.set_text(self.math_opperation)

    def on_press_4(self, button):
        self.math_opperation += "4"
        self.result_entry.set_text(self.math_opperation)

    def on_press_5(self, button):
        self.math_opperation += "5"
        self.result_entry.set_text(self.math_opperation)

    def on_press_6(self, button):
        self.math_opperation += "6"
        self.result_entry.set_text(self.math_opperation)

    def on_press_7(self, button):
        self.math_opperation += "7"
        self.result_entry.set_text(self.math_opperation)

    def on_press_8(self, button):
        self.math_opperation += "8"
        self.result_entry.set_text(self.math_opperation)

    def on_press_9(self, button):
        self.math_opperation += "9"
        self.result_entry.set_text(self.math_opperation)

    def on_press_0(self, button):
        self.math_opperation += "0"
        self.result_entry.set_text(self.math_opperation)

    def on_press_dot(self, button):
        self.math_opperation += ","
        self.result_entry.set_text(self.math_opperation)

    def on_press_plus(self, button):
        self.math_opperation += "+"
        self.result_entry.set_text(self.math_opperation)

    def on_press_minus(self, button):
        self.math_opperation += "-"
        self.result_entry.set_text(self.math_opperation)

    def on_press_multiply(self, button):
        self.math_opperation += "×"
        self.result_entry.set_text(self.math_opperation)

    def on_press_divide(self, button):
        self.math_opperation += "÷"
        self.result_entry.set_text(self.math_opperation)

    def on_press_equal(self, button):
        self.math_opperation = self.math_opperation.replace(",", ".")
        self.math_opperation = self.math_opperation.replace("×", "*")
        self.math_opperation = self.math_opperation.replace("÷", "/")
        self.result = eval(self.math_opperation)
        if type(self.result) is not int:
            digits = int(len(str(self.result).split(".")[1]))
            if digits > 2:
                digits = int(digits/2)
                self.result = round(self.result, digits)
        self.result_entry.set_text(str(self.result).replace(".", ","))
        self.math_opperation=""

    def on_press_ac(self, button):
        self.math_opperation=""
        self.result_entry.set_text("0")
