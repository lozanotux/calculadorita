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
        self.win.present()

def main():
    app = Calculadorita(application_id="com.github.lozanotux.calculadorita")
    app.run(sys.argv)

if __name__ == '__main__':
    main()