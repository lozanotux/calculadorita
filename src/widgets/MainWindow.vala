/*
 * SPDX-License-Identifier: GPL-3.0-or-later
 * SPDX-FileCopyrightText: 2023 Juan Pablo Lozano <lozanotux@gmail.com>
 */

public class MainWindow : Gtk.ApplicationWindow {

    public MainWindow (Gtk.Application application) {
        Object (
            application: application,
            title: Constants.APP_NAME,
            default_width: 300,
            default_height: 400,
            resizable: false
        );
    }

    construct {
        // Main box to pack the rest of widgets
        var main_box = new Gtk.Box (Gtk.Orientation.VERTICAL, 6);
        
        var result_label = new Gtk.Label ("0");

        // Grid section
        var grid = new Gtk.Grid () {
            column_spacing = 6,
            row_spacing = 6
        };

        var ac_button = new Gtk.Button.with_label ("AC");
        // attach () --> (widget, column, row, width. height)
        grid.attach (ac_button, 0, 0, 3, 1);

        var seven_button = new Gtk.Button.with_label ("7");
        var eight_button = new Gtk.Button.with_label ("8");
        var nine_button = new Gtk.Button.with_label ("9");
        grid.attach (seven_button, 0, 1, 1, 1);
        grid.attach (eight_button, 1, 1, 1, 1);
        grid.attach (nine_button, 2, 1, 1, 1);

        var four_button = new Gtk.Button.with_label ("4");
        var five_button = new Gtk.Button.with_label ("5");
        var six_button = new Gtk.Button.with_label ("6");
        grid.attach (four_button, 0, 2, 1, 1);
        grid.attach (five_button, 1, 2, 1, 1);
        grid.attach (six_button, 2, 2, 1, 1);

        var one_button = new Gtk.Button.with_label ("1");
        var two_button = new Gtk.Button.with_label ("2");
        var three_button = new Gtk.Button.with_label ("3");
        grid.attach (one_button, 0, 3, 1, 1);
        grid.attach (two_button, 1, 3, 1, 1);
        grid.attach (three_button, 2, 3, 1, 1);

        var zero_button = new Gtk.Button.with_label ("0");
        var comma_button = new Gtk.Button.with_label (",");
        grid.attach (zero_button, 0, 4, 2, 1);
        grid.attach (comma_button, 2, 4, 1, 1);

        var divide_button = new Gtk.Button.with_label ("÷");
        var multiply_button = new Gtk.Button.with_label ("×");
        var subtract_button = new Gtk.Button.with_label ("−");
        var sum_button = new Gtk.Button.with_label ("+");
        var equal_button = new Gtk.Button.with_label ("=");
        grid.attach (divide_button, 3, 0, 1, 1);
        grid.attach (multiply_button, 3, 1, 1, 1);
        grid.attach (subtract_button, 3, 2, 1, 1);
        grid.attach (sum_button, 3, 3, 1, 1);
        grid.attach (equal_button, 3, 4, 1, 1);

        main_box.append (result_label);
        main_box.append (grid);
        set_child (main_box);
    }

}