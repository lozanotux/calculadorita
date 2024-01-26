# Calculadorita

A calculator app writen in Vala and GTK+ for GNU/Linux by Argentinian guy 🇦🇷 🖱️

![screenshot](./data/media/screenshot1.png)

<a href="https://github.com/lozanotux/calculadorita/tree/main" target="_blank" style="max-width: 100%;background-image: linear-gradient(to bottom, #f5f5f5, #d3d3d3);border-color: rgba(0, 0, 0, .8);box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .02), inset 0 1px 0 0 rgba(255, 255, 255, .2), inset 0 -1px 0 0 rgba(255, 255, 255, .05), 0 3px 6px rgba(0, 0, 0, .16), 0 3px 6px rgba(0, 0, 0, .16);overflow: hidden;transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);color: #000!important;text-shadow: 0 1px rgba(0,0,0,.3);-webkit-appearance: none;border: 1px solid rgba(0,0,0,.2);border-radius: 3px;cursor: pointer;font-family: inherit;font-size: 16px;outline: none;text-align: center;text-decoration: none;">
  <img src="data/media/vala.png" alt="Vala icon" class="launchpad-icon" width="16px">
  Vala Version
</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://github.com/lozanotux/calculadorita/tree/python-version" target="_blank" style="max-width: 100%;background-image: linear-gradient(to bottom, #4d4d4d, #333);border-color: rgba(0, 0, 0, .8);box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .02), inset 0 1px 0 0 rgba(255, 255, 255, .2), inset 0 -1px 0 0 rgba(255, 255, 255, .05), 0 3px 6px rgba(0, 0, 0, .16), 0 3px 6px rgba(0, 0, 0, .23);overflow: hidden;transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);color: #fff;text-shadow: 0 1px rgba(0,0,0,.3);-webkit-appearance: none;border: 1px solid rgba(0,0,0,.2);border-radius: 3px;cursor: pointer;font-family: inherit;font-size: 16px;outline: none;text-align: center;text-decoration: none;">
  <img src="data/media/python.png" alt="Github icon" class="launchpad-icon" width="16px">
  Python 3 Version
</a>
<div id="main-description" class="container-fluid">
           
</div>

## How to build this app locally?

1. Install required dependencies:
  * **Ubuntu:**
    ```bash
    sudo apt install build-essential desktop-file-utils gettext gobject-introspection libgee-0.8-dev libgirepository1.0-dev libglib2.0-dev libgtk-4-dev libxml2-dev libxml2-utils meson cmake valac valadoc libmatheval-dev python3
    ```

2. Configure installation target directory and prepare the source code:
    ```bash
    meson build --prefix=/usr
    ```

3. Compile the source code and install the app on your system:
    ```bash
    cd build
    ninja
    ninja install
    ```

# Uninstall this app from you system?

To remove the application files from your system, run next command from the root of the project:
```bash
sudo ninja -C build uninstall
```