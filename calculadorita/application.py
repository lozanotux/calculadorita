import calculadorita.constants as constants
import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk
from calculadorita.widgets.main_window import MainWindow


class Calculadorita(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('../data/application.css')
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.win = MainWindow(
            application=app,
            title=constants.APP_NAME,
            default_width=300,
            default_height=400,
            resizable=False
        )

        self.key_controller = Gtk.EventControllerKey()
        self.key_controller.connect('key-pressed', on_key_event, self.win)
        self.win.add_controller(self.key_controller)

        self.win.present()

def on_key_event(keyval, keycode, state, user_data, win):
    if keycode == 48 or keycode == 65456:
        win.on_press_0(win.zero_button)
    elif keycode == 49 or keycode == 65457:
        win.on_press_1(win.one_button)
    elif keycode == 50 or keycode == 65458:
        win.on_press_2(win.two_button)
    elif keycode == 51 or keycode == 65459:
        win.on_press_3(win.three_button)
    elif keycode == 52 or keycode == 65460:
        win.on_press_4(win.four_button)
    elif keycode == 53 or keycode == 65461:
        win.on_press_5(win.five_button)
    elif keycode == 54 or keycode == 65462:
        win.on_press_6(win.six_button)
    elif keycode == 55 or keycode == 65463:
        win.on_press_7(win.seven_button)
    elif keycode == 56 or keycode == 65464:
        win.on_press_8(win.eight_button)
    elif keycode == 57 or keycode == 65465:
        win.on_press_9(win.nine_button)
    elif keycode == 44 or keycode == 46:
        win.on_press_dot(win.comma_button)
    elif keycode == 47 or keycode == 65455:
        win.on_press_divide(win.divide_button)
    elif keycode == 42 or keycode == 65450:
        win.on_press_multiply(win.multiply_button)
    elif keycode == 43 or keycode == 65451:
        win.on_press_plus(win.sum_button)
    elif keycode == 45 or keycode == 65453:
        win.on_press_minus(win.subtract_button)
    elif keycode == 61:
        win.on_press_equal(win.equal_button)
    elif keycode == 65307:
        win.on_press_ac(win.ac_button)

def main():
    app = Calculadorita(application_id="com.github.lozanotux.calculadorita")
    app.run(sys.argv)

if __name__ == '__main__':
    main()