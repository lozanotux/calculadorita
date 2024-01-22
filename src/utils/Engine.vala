/*
 * SPDX-License-Identifier: GPL-3.0-or-later
 * SPDX-FileCopyrightText: 2023 Juan Pablo Lozano <lozanotux@gmail.com>
 */

public class Engine {

    /*
     * I decided to use a call to a function in python that does the same
     * thing, since it works much better and since nowadays almost every
     * GNU/Linux distribution comes with python already installed we can 
     * execute an inline command
     */
    public static string eval_math_expression (string expression) {
        // Normalize certain symbols to match with expected symbols
        string normalized_expression = expression.replace (",", ".");
        normalized_expression = normalized_expression.replace ("×", "*");
        normalized_expression = normalized_expression.replace ("÷", "/");

        // Now evaluate the expression and get the result
        string result;

        try {
            string command_error;
            GLib.Process.spawn_command_line_sync (
                "python3 -c 'r=eval(\"" + normalized_expression + "\");print(r) if type(r) == int else print(round(r,2))' 2> /dev/null",
                out result,
                out command_error
            );
            
            if (command_error != "") {
                result = normalized_expression.substring (0, normalized_expression.length - 1);
            }
        } catch (GLib.Error e) {
            warning ("Error executing python eval() function: %s", e.message);
            result = "Error";
        }

        // Replace dot with comma to make it look better
        result = result.replace (".", ",");
        message ("Doing operation [ %s ] - Result: %s", normalized_expression, result);

        /* 
         * The eval() function when it works with decimal numbers and
         * the result is an integer also shows a 0 after the comma, so
         * to make it look better it is eliminated
         */
        if ("," in result) {
            string[] splited_result = result.split (",");
            if (int.parse(splited_result[1]) == 0) {
                result = splited_result[0];
            }
        }
        
        return result.strip ();
    }

}